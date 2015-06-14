# TocHw3

## 前言
這是我在計算理論這門課的第一份程式作業，因為前兩份是手寫，因此代號是Hw3<br>
作業要求是要我們在Json-like的資料中，找到每一個Web的對外超連結數量是多少。<br>
在作業說明中提示可以使用 module: json, re。

## 檔案說明
在這個作業中有四個檔案:
* input.txt: 這是老師提供的sample資料
* tocHw3.py: 這個為主要的程式碼，只有一個檔案。
* hw3.pdf:   作業要求及說明。
* README.md: 即此份說明文件。

## 執行方法
```
python tocHw3.py inputfile request_top_k
```

## 編寫想法
在這一次的作業中，我嘗試了兩種不同的方法：
* 單純使用 json:
* 單純使用 regex:
原本我是使用json module下去寫這份作業，但是發現速度實在是太慢了<br>
於是，後來使用regex。據說python在實作regex的時候，是使用和C語言一樣的實作方式<br>
所以，可預期的是這速度會比原本使用json module還要來得快得多！<br><br>

如果想要查看json版本的原始碼可以clone到本機端之後，使用：<br>
```
git checkout b97829a
```
執行tocHw3.py這個檔案即可，雖然好像有一個微小的bug，就是這個版本在計算outlink number的時候，<br>
是用built-in function: len( ) 去取得整個 "Links" 標籤內的內容，但是100比資料中，似乎有一筆資料的標籤並不包含<br>
“href" 或是 "url" 導致那一筆資料的outlink數會差1。
