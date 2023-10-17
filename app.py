
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 補助金の対象外経費のリスト
NON_ELIGIBLE_EXPENSES = [
    "既存事業活用","家賃","保証金","敷金","仲介手数料","光熱水費","諸経費","会社経費","一般管理費","現場管理費",
    "雑費","詳細不確認経費","フランチャイズ加盟料","電話代","インターネット利用料金","通信費","クラウドサービス利用費",
    "商品券","金券","原材料費","予備品購入費","事務用品","消耗品代","雑誌購読料","新聞代","団体会費","飲食",
    "奢侈","娯楽","接待","不動産購入費","構築物購入費","株式購入費","税務申告","決算書作成","税理士費用",
    "公認会計士費用","訴訟費用","弁護士費用","登記","登録","特許","免許","許可","検査","検定","試験","証明",
    "公文書交付","手数料","収入印紙","振込手数料","代引手数料","両替手数料","公租公課","消費税","地方消費税",
    "保険料","支払利息","遅延損害金","書類作成費用","書類提出費用","事務用PC","プリンタ","文書作成ソフトウェア",
    "タブレット端末","スマートフォン","デジタル複合機","診療報酬","介護報酬","家具","自動車","車両","船舶",
    "航空機","修理費","車検費用","中古機械設備","中古品購入費","人件費","旅費","観光農園","栽培経費",
    "再生可能エネルギー","発電設備","ソーラーパネル","助成制度","補助金","委託費","公的医療保険","介護保険",
    "診療報酬","介護報酬","固定価格買取制度","市場価格乖離","社会通念不適切経費"
    # ... 他のキーワードも追加できます
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_expense():
    expense = request.form['expense']
    message = ""
    message_type = "success"

    if expense.lower() in NON_ELIGIBLE_EXPENSES:
        message = f"{expense}は補助金の対象外経費です"
        message_type = "danger"
    else:
        message = f"{expense}は補助金の対象経費です（詳細は各補助金のガイドラインを確認してください）"

    return render_template('result.html', message=message, message_type=message_type)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    term = request.args.get('term', '')
    suggestions = [word for word in NON_ELIGIBLE_EXPENSES if term.lower() in word.lower()]
    return jsonify(suggestions)

@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form['feedback']
    print("User feedback received:", user_feedback)
    return "Feedback received", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
