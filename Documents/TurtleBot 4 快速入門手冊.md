# TurtleBot4 快速入門使用手冊

![](https://turtlebot.github.io/turtlebot4-user-manual/media/TurtleBot4.jpg)

TurtleBot 4 是一款基於 ROS2 的移動機器人並以用於教學及研究為旨。TurtleBot 4 有著能夠繪製機器人周遭的地圖、自主導航、在相機上運行人工智能模組等功能。

它使用 Create 3 作為移動底座，並在上面放置已建構 TurtleBot 4 軟體的Raspberry Pi 4B。

使用 RPLIDAR A1M8 360度光達 以及 Luxonis OAK-D 鏡頭作為感測元件。

<!-- ## 資源

### 軟體

#### Ubuntu
- Ubuntu 20.04 LTS Desktop (Focal Fossa) : https://releases.ubuntu.com/20.04/
- Ubuntu 22.04 LTS Desktop (Jammy Jellyfish) : https://releases.ubuntu.com/22.04/

#### Raspberry Pi
- 映像檔燒入 Raspberry Pi Imager : https://www.raspberrypi.com/software/
- 腳位定義 Raspberry Pi Pinout : https://pinout.xyz/

#### ROS2
- 

#### TurtleBot4

#### iRobot® Create® 3

#### Luxonis

#### SLAMTEC -->

# 基本設定

為了能更快速的上手 TurtleBot 4，使用者需準備一台具有連接 WiFi 功能並能安裝 Ubuntu 的筆記型電腦以及能夠提供連線的 WiFi 分享器或環境。

## 使用者 PC

### 安裝 ROS2

建議選用與車子相對應版本的 Ubuntu Desktop 並且安裝 ROS2。

- ROS2 Galactic

    - 作業系統要求：[Ubuntu 20.04](https://releases.ubuntu.com/20.04/)
    - 使用腳本安裝ROS2：
    
        ```
        wget -c https://raw.githubusercontent.com/zhl017/ros_install_noetic/zhl017/ros2_install_galactic.sh && chmod +x ./ros2_install_galactic.sh && ./ros2_install_galactic.sh
        ```
    - 安裝ROS2後，安裝相關套件：
    
        ```
        sudo apt install ros-galactic-turtlebot4-desktop \
        ros-galactic-turtlebot4-msgs \
        ros-galactic-turtlebot4-navigation \
        ros-galactic-turtlebot4-node
        ```
- ROS2 Humble

    - 作業系統要求：[Ubuntu 22.04](https://releases.ubuntu.com/22.04/)
    - 使用腳本安裝 ROS2：
    
        ```
        wget -c https://raw.githubusercontent.com/zhl017/ros_install_noetic/zhl017/ros2_install_humble.sh && chmod +x ./ros2_install_humble.sh && ./ros2_install_humble.sh
        ```
    - 安裝 ROS2 後，安裝相關套件：
    
        ```
        sudo apt install ros-humble-turtlebot4-desktop \
        ros-humble-turtlebot4-msgs \
        ros-humble-turtlebot4-navigation \
        ros-humble-turtlebot4-node \
        ros-humble-rmw-cyclonedds-cpp
        ```
        
### 編輯環境變數文件 bashrc

要編輯bashrc文件需要在 PC 上開啟終端機輸入：

```
nano ~/.bashrc
```

在文件最底部加上下列命令 (若重複命令則省略) ：

```
source /opt/ros/galactic/setup.bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export ROS_DOMAIN_ID=0
export CYCLONEDDS_URI='<CycloneDDS><Domain><General><DontRoute>true</></></></>'
```
`ctrl + o`儲存`ctrl + x`離開
    
重新載入環境變數，在終端機輸入：

```
source ~/.bashrc
```

---

## 機器人移動平台

設置TurtleBot 4 第一步是先開啟電源並連接到 WiFi。

### 開啟電源

將 TurtlrBot 4 放置於充電底座上，數秒後車子 LED 指示燈會亮起並成功開機。

關於 Create3 上的按鈕與 LED 指示燈的更多詳細訊息，請參考[Create3網頁](https://iroboteducation.github.io/create3_docs/hw/face/)

### 首次連接

當首次開啟 TurtleBot 4 時，Raspberry Pi 預設開啟 AP 模式，使用者可使用 PC 直接連接上它。

> **WiFi名稱：Turtlebot4**
> **WiFi密碼：Turtlebot4**

> TurtleBot 4 AP 網路預設為 5GHz，使用者需使用支援連接 5GHz WiFi 的設備才能進行連接。

成功連上 WiFi 後，可透過 SSH 連接到 Raspberry Pi 上進行網路設定。在 PC 上開啟終端機輸入：

```
ssh ubuntu@10.42.0.1
```

> **遠端密碼：turtlebot4**

---

## 網路設定

透過連接 AP 模式設定 Create 3 與 Raspberry Pi 連接到 WiFi 網路。

### 將 Create 3 連接到 WiFi 網路

> Create 3 只支援連接到 2.4GHz WiFi 網路

透過開啟網頁並輸入 Raspberry Pi IP 的 8080 Port **(10.42.0.1:8080)** 進入 Create 3 的網路服務器。

![](https://hackmd.io/_uploads/HkgBA_2a2.png)

![](https://turtlebot.github.io/turtlebot4-user-manual/setup/media/webserver_home.png)

在左上工具列選擇 **Connect** 選項，輸入要連接的 WiFi 名稱與密碼後點擊確認鍵。

![](https://turtlebot.github.io/turtlebot4-user-manual/setup/media/create3_connect.png)

等待連接到 WiFi 並撥放提示音，重新整理網頁檢查 **Connect** 頁面上方是否顯示IP位址。

### 將 Raspberry Pi 連接到 WiFi 網路

> 將 Raspberry Pi 連接至 5GHz 網路能獲得最佳性能。

SSH 登入後，在 SSH 視窗中輸入要連接的 WiFi 名稱與密碼幫助 Raspberry Pi 進行連接：
```
sudo wifi.sh -s '<WIFI_SSID>' -p '<WIFI_PASSWORD>' && sudo reboot
```

範例：

假設要連接上的 WiFi 為`example`，密碼為`123456`，需要輸入：
```
sudo wifi.sh -s example -p 123456 && sudo reboot
```

待 Raspberry Pi 重開機並撥放提示音後，將 PC 連接到相同 WiFi 網路打開終端機輸入指令觀察是否成功取得 Raspberry Pi 與 Create 3資料：

```
ros2 topic list
```

透過下列指令取得 Raspberry Pi IP 位址：

```
ros2 topic echo /ip
```

---

# 基本應用

下列指令都在 PC 上執行

## 關閉電源

將 TurtleBot 4 移開充電座並按壓住正中間按鈕直到發出關機提示音。

---

## rqt 監控視窗

觀看 TurtleBot 4 主題是否正常執行

    ros2 launch turtlebot4_diagnostics diagnostics.launch.py
    
![](https://turtlebot.github.io/turtlebot4-user-manual/troubleshooting/media/diagnostics.png)

---

## 遙控 TurtleBot 4

使用 PC 鍵盤遙控 TurtleBot 4

    ros2 run teleop_twist_keyboard teleop_twist_keyboard

若無法執行或是出現錯誤，請安裝`teleop_twist_keyboard`套件：

- Galactic

    ```
    sudo apt install ros-galactic-teleop-twist-keyboard
    ```
    
- Humble

    ```
    sudo apt install ros-humble-teleop-twist-keyboard
    ```
    
![](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/media/teleop_twist_keyboard.png)

---

## 繪製地圖 (SLAM)

### 啟動 SLAM

SLAM 是用於繪製機器人周為環境地圖及定位的技術，在 TurtleBot 4 中使用 **slam_toolbox** 將來自 Create 3 的里程數據以及 RPLIDAR 的光達掃描數據相結合來生成地圖。

在 PC 上開啟終端機輸入：

    ros2 launch turtlebot4_navigation slam_sync.launch.py
    
### 啟動 Rviz2

在 PC 上開啟終端機輸入：

    ros2 launch turtlebot4_viz view_robot.launch.py
    
![](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/media/rviz_slam.png)

### 遙控 TurtleBot 4

請參考遙控教學。

### 保存地圖

在 PC 上開啟終端機輸入：

    ros2 run nav2_map_server map_saver_cli -f map
    
這將會在當前目錄下產生 **map.pgm** 與 **map.yaml** 兩個地圖相關文件。

---

## 導航

### SLAM vs Localization

這邊可以使用兩種方法來確認機器人在地圖上的位置：SLAM 或 Localization。

SLAM 允許我們在導航時生成地圖，而 Localization 則需要有一張已存在的地圖。

- SLAM：對於生成新地圖或在未知或動態環境中的導航很有幫助，這可以使地圖在即時檢測的時候產生變化，但缺點是無法看到尚未生成的地圖區域。

- Localization：使用現有地圖及實際里程計與光達掃描數據來進行定位，雖然地圖不會因為環境產生變化而更新地圖，但仍舊可以在導航時避開偵測到的新的障礙，也因為地圖不會變化所以可以得到許多不同路徑的導航結果。

### 啟動導航

這邊使用 localization 進行導航。

在 PC 上開啟終端機輸入：

    ros2 launch turtlebot4_navigation nav_bringup.launch.py slam:=off localization:=true map:=map.yaml

請自行替換map.yaml名稱。

### 啟動 Rviz2

在 PC 上開啟終端機輸入：

    ros2 launch turtlebot4_viz view_robot.launch.py

![](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/media/office.png)

視窗上排有幾種工具可使用

![](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/media/nav_tools.png)

- 2D Pose Estimate：用於定位，設置機器人在地圖上的大概位置。

    ![](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/media/pose_estimate.gif)

- Publish Poinst：可以單點一個位置並將該點發佈到話題`/clicked_point`。

    可以在 PC 上開啟終端機輸入指令查看：
    
    ```
    ros2 topic echo /clicked_point
    ```
    
    ![](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/media/clicked_point.gif)
    
- Nav2 Goal：替機器人發送目標讓機器人嘗試抵達，在發送目標前請先定位機器人位置。

    ![](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/media/nav_goal.gif)

---

# 常見問題

## PC 看不到話題

確定 PC Raspberry Pi 、 Create 3 都在相同網路環境底下執行 `ros2 topic list` 還是看不到話題，在 PC 開啟終端機輸入：

    ros2 daemon stop

將 PC 其他網路連線關閉或移除 (網路線)後，再次輸入：

    ros2 topic list

---

## Raspberry Pi 沒有正常啟動 turtlebot4 node

使用 SSH 進入 Raspberry Pi 重新啟動程式，在 SSH 視窗中輸入：

    sudo systemctl restart turtlebot4.service

---
