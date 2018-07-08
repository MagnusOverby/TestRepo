import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.metrics import roc_auc_score

# ================================================================= #
# ==== this document contains mainly functions form the Lopez book  #
# ================================================================= #


def fracDiff_Lim(series, d, thres=.01):
    w = np.array(getWeights_FED(d, thres))

    width = len(w) - 1
    df = {}
    seriesF, df_ = series.fillna("pad"), {}
    for iloc in range(width, seriesF.shape[0]):
        loc0, loc1 = seriesF.index[iloc - width], seriesF.index[iloc]
        # Thats essentially just so i can use loc instead of iloc, has no real effect, a pandas trick.

        df_[loc1] = np.dot(w.T, seriesF.loc[loc0:loc1])
        # print(df_[loc1])

    df = pd.Series(df_)

    return df


def getWeights_FED(d, tresh=.01):
    w = [1.]
    k = 1
    while True:
        w_ = -w[-1] / k * (d - k + 1)
        if np.abs(w_) < tresh: return w
        w.append(w_)
        k += 1

#=================================================================================#
# ========= BELOW ARE NON MULTI THREADED VERSION OF THE CODE =====================#
# ============== THIS CODE IS MAINLY FOR LABELING TO TEST DIFFERENT TECNIQUES ====#
#=================================================================================#

def applyPtSlOnT1(close, events, ptSl):
    # dont bother with this multithreading stuff for now
    events_ = events

    out = events_[["t1"]].copy(deep=True)

    if ptSl[0] > 0:

        pt = ptSl[0] * events_["trgt"]

    else:

        pt = pd.Series(index=events.index)

    if ptSl[1] > 0:
        sl = -ptSl[1] * events_["trgt"]
    else:
        sl = pd.Series(index=events.index)

    for loc, t1 in events_["t1"].fillna(close.index[-1]).iteritems():
        df0 = close[loc:t1]
        df0 = (df0 / close[loc] - 1)  # *events_at[loc,"side"] #Not sure how this actually works...
        out.loc[loc, "sl"] = str(df0[df0 < sl[loc]].index.min())
        out.loc[loc, "pt"] = str(df0[df0 > pt[loc]].index.min())
    return out


# ===== THIS IS JUST A HACKY HELPER FUNCTIONS FOR HANDELING NaNs in Timestamps ===========#

def hackTimeStampMinDropNa(tb_test):
    output = []
    large_date = pd.datetime(2100, 1, 1)

    for i in range(0, tb_test.shape[0]):
        a = tb_test.iloc[i, 0]
        b = tb_test.iloc[i, 1]
        c = tb_test.iloc[i, 2]

        if "NaT" in str(a):
            a = large_date
        if "NaT" in str(b):
            b = large_date
        if "NaT" in str(c):
            c = large_date

        output.append(min(pd.to_datetime(a), pd.to_datetime(b), pd.to_datetime(c)))

    return output

# ====================================================================================== #
# ======== THIS FUNCTION GET THE DIFFERENT BINS WHERE WE CLASSIFY EACH OBSERVATIONS ==== #
# ====================================================================================== #

def getBins(events, close):
    # we drop all the na on the t1
    events_ = events.dropna(subset=["t1"])
    # print(events)
    px = events_.index.union(pd.to_datetime(events_["t1"])).drop_duplicates()
    # we add all the t1 to the event indexes and drop the duplicates which will show up.

    px = close.reindex(px, method="bfill")
    # 2 create the outpupx.lt

    out = pd.DataFrame(index=events_.index)
    out["ret"] = px.loc[events_["t1"]].values / px.loc[events_.index].values - 1

    out["bin"] = np.sign(out["ret"]) * (1 - (out.index == events_["t1"]))
    if "side" in events_:
        out["ret"] *= events_["side"]
        out.loc[out["ret"] <= 0, "bin"] = 0
        out.loc[out["ret"] > 0, "bin"] = 1



    return out


# =============================================================== #
#                          Seems to work.
#                   Now write the getEvents function
# =============================================================== #

def getEvents(close, tEvents, ptSl, trgt, minRet, numThreads, t1=False,side=None):
    # get target
    trgt = trgt.loc[tEvents]
    trgt = trgt[trgt > minRet]
    if t1 is False: t1 = pd.Series(pd.NaT, index=tEvents)

    # add Sides to this for meta labeling purposes
    if side is None:

        side_, ptSl_ = pd.Series(1.0, index=trgt.index), [ptSl[0], ptSl[0]]

    else:

        side_, ptSl_ = side.loc[trgt.index], ptSl[:2]

    events = pd.concat({"t1": t1, "trgt": trgt, "side": side_}, axis=1).dropna(subset=["trgt"])
    df0 = applyPtSlOnT1(close, events, ptSl=ptSl)
    events["t1"] = hackTimeStampMinDropNa(df0)
    events = events.drop("side", axis=1)
    return events


def get_bins(t_sig, ts,minret=0):
    side = t_sig
    # We stop out after 10 days no matter what !
    close = ts
    close.index.tz_localize(None)
    tEvents = close.index[::5]
    ptSl = []
    ptSl.append(0)
    ptSl.append(0.06)
    t1 = False
    trgt = getDailyVol(ts, 30)

    # now get tripper barrier !!

    trippelb = getEvents(ts, tEvents, ptSl, trgt, minret, 1, t1)
    trippelb["side"] = t_sig
    bins = getBins(trippelb, ts).dropna()

    return bins


def getDailyVol(close,span0=100):
    df0 = close.index.searchsorted(close.index-pd.Timedelta(days=1))
    df0=df0[df0>0]
    df0=pd.Series(close.index[df0-1],index=close.index[close.shape[0]-df0.shape[0]:])
    df0 = close.loc[df0.index]/close.loc[df0].values-1 #these are daily returns
    df0=df0.ewm(span0).std()
    return df0


# Compute nessesary statistics
# def computeRecall(predict,bins)

def pred_stats(predic, bi):

    # ===== The confusion matrix printed out ====== #
    tp = float(np.sum((predic == 1) & (bi == 1)))
    fp = float(np.sum((predic == 1) & (bi == 0)))
    fn = float(np.sum((predic == 0) & (bi == 1)))
    tn = float(np.sum((predic == 0) & (bi == 0)))

    recall = tp / (tp + fn)
    accuracy = (tp + tn) / (fn + fp + tp + tn)
    F1 = 2 / (1 / recall + 1 / accuracy)
    print(recall)
    print(accuracy)
    print(F1)
    auc = roc_auc_score(predic, bi)
    return [F1, recall, accuracy, auc]


# ============= Building pseudo volume bars =================
#
# takes : a dataframe consisting price volume and index is dates
# ouputs : a dollar sampled price
#
# ===========================================================
def build_volume_series(df, idx):
    d_out = df.copy("deep")

    d_vol = df.iloc[:, idx]

    d_denom = d_vol.groupby(lambda x: x.date).transform(np.mean)

    d_cum = d_denom.cumsum()

    arr_t = np.digitize(d_vol.cumsum(), d_cum) - 1

    nDex = d_out.index[arr_t]

    d_out["dollarsum"] = d_out.iloc[:, 0] * d_out.iloc[:, 1]

    d_out = d_out["dollarsum"].groupby(lambda x: x).agg(np.sum) / d_out.iloc[:, 1].groupby(lambda x: x).agg(np.sum)

    return d_out


def build_price_volume(vol_s, price_s):
    pass
