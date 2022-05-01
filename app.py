import flask
import pickle
import pandas as pd

# using pickle to load in the pre-trained neural network model
with open(f'model/model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')


@app.route('/')
def main():
    if flask.request.method == "GET":
        return flask.render_template('main.html')

    if flask.request.method == "POST":
        sequence = flask.request.form['sequence']

        inputVariables = fillDataFrame(sequence)
        prediction = model.predict(inputVariables)[0]
        return flask.render_template('main.html', original_input={'Sequence': sequence}, result=prediction)


def fillDataFrame(seq):
    ae = 1
    aa = 1
    ad = 1
    af = 1
    ag = 1
    aj = 1
    ee = 1
    ea = 1
    ed = 1
    ef = 1
    eg = 1
    ej = 1
    de = 1
    da = 1
    dd = 1
    df = 1
    dg = 1
    dj = 1
    fe = 1
    fa = 1
    fd = 1
    ff = 1
    fg = 1
    fj = 1
    ge = 1
    ga = 1
    gd = 1
    gf = 1
    gg = 1
    gj = 1
    je = 1
    ja = 1
    jd = 1
    jf = 1
    jg = 1
    jj = 1
    if "ae" not in seq:
        ae = 0
    if "aa" not in seq:
        aa = 0
    if "ad" not in seq:
        ad = 0
    if "af" not in seq:
        af = 0
    if "ag" not in seq:
        ag = 0
    if "aj" not in seq:
        aj = 0
    if "ee" not in seq:
        ee = 0
    if "ea" not in seq:
        ea = 0
    if "ed" not in seq:
        ed = 0
    if "ef" not in seq:
        ef = 0
    if "eg" not in seq:
        eg = 0
    if "ej" not in seq:
        ej = 0
    if "de" not in seq:
        de = 0
    if "da" not in seq:
        da = 0
    if "dd" not in seq:
        dd = 0
    if "df" not in seq:
        df = 0
    if "dg" not in seq:
        dg = 0
    if "dj" not in seq:
        dj = 0
    if "fe" not in seq:
        fe = 0
    if "fa" not in seq:
        fa = 0
    if "fd" not in seq:
        fd = 0
    if "ff" not in seq:
        ff = 0
    if "fg" not in seq:
        fg = 0
    if "fj" not in seq:
        fj = 0
    if "ge" not in seq:
        ge = 0
    if "ga" not in seq:
        ga = 0
    if "gd" not in seq:
        gd = 0
    if "gf" not in seq:
        gf = 0
    if "gg" not in seq:
        gg = 0
    if "gj" not in seq:
        gj = 0
    if "je" not in seq:
        je = 0
    if "ja" not in seq:
        ja = 0
    if "jd" not in seq:
        jd = 0
    if "jf" not in seq:
        jf = 0
    if "jg" not in seq:
        jg = 0
    if "jj" not in seq:
        jj = 0
    return pd.DataFrame([ae, aa, ad, af, ag, aj, ee, ea, ed, ef, eg, ej, de, da, dd, df, dg, dj, fe, fa, fd, ff, fg, fj,
                         ge, ga, gd, gf, gg, gj, je, ja, jd, jf, jg, jj], columns=['ae', 'aa', 'ad', 'af', 'ag', 'aj',
                                                                                   'ee', 'ea', 'ed', 'ef', 'eg', 'ej',
                                                                                   'de', 'da', 'dd', 'df', 'dg', 'dj',
                                                                                   'fe', 'fa', 'fd', 'ff', 'fg', 'fj',
                                                                                   'ge', 'ga', 'gd', 'gf', 'gg', 'gj',
                                                                                   'je', 'ja', 'jd', 'jf', 'jg', 'jj'],
                        dtype=float)


if __name__ == '__main__':
    app.run()
