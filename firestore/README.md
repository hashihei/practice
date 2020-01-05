---
## Firestoreの操作(Python)
### snippets.py
* 最初のプログラム。
1. データの追加 
2. データの一括読み出し

### set_document.py
データ更新の操作について。Fire Storeでは1つのドキュメントを更新できる回数は1回/sec なので注意が必要。この頻度を超える場合は、分散カウンタの利用を検討する必要がある。分散カウンタではシャドーの数がパフォーマンスに影響を与える点と、コストに影響を与えるため、注意が必要。
1. シンプルなデータの追加
2. ネストしたデータの追加
3. IDを自動で取得してデータを追加
4. データの更新

[Cloud Firestoreにデータを追加する](https://firebase.google.com/docs/firestore/manage-data/add-data?hl=ja)
---