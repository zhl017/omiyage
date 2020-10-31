# Install fcitx + chewing 新酷音輸入法
## Installation
1. 安裝框架
```
sudo apt-get install fcitx fcitx-chewing
```

2. 調整fcitx為預設輸入法

**System Setting** > **Language Support** > **Language** > **Keyboard input method system** > Select **fcitx**

3. Log out Ubuntu

4. 調整個程式獨立輸入法

**System Settings** > **Text Entry** > Select **Allow different sources for each application**

5. 取消選字框

右上輸入法圖示 > **Configure** > **Global Config** > **Show Advence Option** > **Appearance** > Select **Do not show input window if there is only preedit string**

6. 變更輸入法圖示![](https://raw.githubusercontent.com/zhl017/omiyage/main/%E6%96%B0%E9%85%B7%E9%9F%B3/fcitx-chewing.png) (右鍵另存圖片)
```
 sudo cp fcitx-chewing.png /usr/share/icons/hicolor/48x48/apps/fcitx-chewing.png
```

## Reference
* https://medium.com/gcc-me-c/fcitx-chewing-%E6%96%B0%E9%85%B7%E9%9F%B3%E4%B8%AD%E6%96%87%E8%BC%B8%E5%85%A5%E6%B3%95%E5%AE%89%E8%A3%9D-7f06b16b3e51
* https://gist.github.com/tanyuan/c0d4ee15cf0c9c93da28cc1cf0ff87b3
