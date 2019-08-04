## 使い方
- 実行すると5つのウィンドウが表示される．「click」ウィンドウの任意の場所Aを左クリックすると，Aを頂点とする一辺20ピクセルの領域が白くなり，その範囲の逆変換を行い，「ifft_single」ウィンドウに表示する．一連の処理はクリックするごとに行われ，「click」ウィンドウの白い部分は増えてゆく．毎回の逆変換の累積画像を，「ifft」ウィンドウに表示する．右クリックするとすべてのウィンドウが閉じ，実行が終了する．
## 実行の仕方
- コマンドプロンプトでAnacondaのパスをsetし、python fimename.pyで実行ファイルを実行する
## 依存ライブラリとバージョン
- openCV 4.1.0
- matplotlib 3.0.3
- numpy 1.16.2
## 参考にしたサイト
- フーリエ変換
    - URL:https://www.slideshare.net/ginrou799/ss-46355460 [フーリエ変換と画像圧縮の仕組み]
- numpyとopenCVを使った画像のフーリエ変換と逆変換
    - URL:https://www.hello-python.com/2018/02/16/numpy%E3%81%A8opencv%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E7%94%BB%E5%83%8F%E3%81%AE%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9B%E3%81%A8%E9%80%86%E5%A4%89%E6%8F%9B/ [numpyとopenCVを使った画像のフーリエ変換と逆変換 – Python in the box]
- 2次元フーリエ変換，フーリエ逆変換(C++)
    - URL:http://opencv.jp/opencv2-x-samples/2d_dft_idft [2次元フーリエ変換，フーリエ逆変換 | OpenCV.jp]
- How to Create a Fourier image
    - URL:https://www.youtube.com/watch?v=gJ2m0dd7QpU [Python 3 Tutorial: Creating a Fourier image - YouTube]
- マウスイベントの処理
    - URL:http://whitecat-student.hatenablog.com/entry/2016/11/09/225631 [OpenCVで表示した画像にマウスクリックした場所を取得する方法 (Python) - 白猫学生のブログ]
- 動画のクロッピング
    - URL:http://sugoiuwasa.jp/%E5%8B%95%E7%94%BB%E3%81%AE%E5%BF%85%E8%A6%81%E9%83%A8%E5%88%86%E3%81%AE%E3%81%BF%E3%82%AF%E3%83%AD%E3%83%83%E3%83%97%EF%BC%88%E5%88%87%E3%82%8A%E6%8A%9C%E3%81%8D%E3%80%81%E3%83%88%E3%83%AA%E3%83%9F/ [動画の必要部分のみクロップ（切り抜き、トリミング）するフリーソフト！]
- mp4からgifへの変換
    - URL:https://convertio.co/ja/mp4-gif/MP4 [ GIF 変換。オンライン フリー — Convertio]
- Githubへのgifアニメーションの貼り付け
    - URL:http://uchimanajet7.hatenablog.com/entry/2017/08/14/083001[GitHub のREADME にgif 画像を表示する1番簡単な方法 #github #gif - uchimanajet7のメモ]
    
## 実行の様子(gifアニメーション)
![Video_19-08-05](https://user-images.githubusercontent.com/52147503/62428920-a70ecb80-b742-11e9-8544-0c64c4e907fe.gif)
