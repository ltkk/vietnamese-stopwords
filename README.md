# Danh sách stopwords tiếng việt
Xây dựng danh sách stopword từ hơn 500k bài viết của wiki

# Dữ liệu
- Dữ liệu Wiki dump tiếng việt gồm hơn 500.000 bài viết(15/01/2019) `viwiki-latest-pages-articles.xml.bz2`
- Bạn có thể download bộ dữ liệu này tại đây
```text
https://dumps.wikimedia.org/viwiki/latest/
```
- Thực hiện tiền xử lý dữ liệu:
    - Parse xml wiki data(Tham khảo: https://radimrehurek.com/gensim/scripts/segment_wiki.html)
    - Sửa lỗi font tiếng Việt
    - Chuẩn hóa dấu câu(https://vi.wikipedia.org/wiki/Quy_tắc_đặt_dấu_thanh_trong_chữ_quốc_ngữ)
    - Tokenize(Sử dụng VNCoreNLP)
    - Loại bỏ các common token: email, phone, emoij, number,...

# Xây dựng bộ stopwords
- Thực hiện tính toán IDF cho tất cả các từ trong tập dữ liệu
- Xuất ra các từ có IDF <= threshold(mình đang để là 3). Trong bộ dữ liệu này (minIDF, maxIDF) = (1.0086982995413565, 13.504312537543813)
- Bạn có thể sửa thông số threshold này cho phù hợp với bài toán của mình

# Sử dụng dữ liệu của bạn
- Sử dụng file make_stopwords.py
