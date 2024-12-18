### 模板設計目的
簡單建立一個網頁頁面套用模板，方便未來開發者在開發頁面時可以直接套用

### 模板組成
> app.py\
建立基本路徑及專案運行

> templates
>>base.html\
最基本的 html 模板，首頁的 html 檔案(label.html)是基於這個模板設計\
>
>>label.html\
首頁的 html 檔案，每一個功能的第一層項目層級的頁面是基於這個進行延伸\
>
>>page.html\
為功能底下頁面層級的基礎擋。如果首頁點進去為頁面，則該頁面的模板須以這個檔案為基礎延伸

>static
用於存放靜態檔案
>>base.css\
為所有頁面的 style 檔
>
>>page.css\
為頁面的 style 檔

### 如何使用這個模板專案
__當首頁有新的功能要開發時__\
__Step 1__ 在 templates 中建立新的資料夾，專門存放該功能的 HTML 檔\
__Step 2__ 在最外層的 layer.html 檔案中建立新的 `<li>` 元素

__如果預設從首頁進入該功能會直接進入頁面__\
__Step 1__ 建立 page 的 HTML 檔案\
__Step 2__ 使其衍伸自 page.html，並修改其中的 `breadcrumb`\
(可以參考 Function_3 的作法)

__如果從首頁進入該功能，功能底下有子項目__\
__Step 1__ 在功能資料夾中建立一個基本 HTML 檔案(如: Function_1 中的 layer.html)，並使其衍伸自 layer.html。記得修改裡面的 `left_bar` 內容，將該功能的子項目選單建立好選項及路徑

__Step 2__ 建立子項目的 HTML 檔案，使其繼承自功能資料夾中的基本 HTML 檔案。修改 `left_bar` 內容，使其包含該項目底下可點及進入的子功能或子頁面。修改 `breadcrumb`，使其包含當前頁面的連結

__Step 3__ 不論子功能底下是功能還是頁面，建立好 HTML 檔案之後都要繼承上一層的 HTML 檔案
- 如果子項目底下是頁面，則須編輯 `menuButton` 和 `siteMenu` 的部分，同時，必須將 `style` 的部分 link 到 page.css\
(這邊可以參考 Function_1 的作法)
- 如果子項目底下是功能，則須編輯 `left_bar` 以及 `breadcrumb` 的部分\
(這邊可以參考 Function_2 的作法)
