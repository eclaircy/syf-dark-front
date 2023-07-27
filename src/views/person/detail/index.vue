<template>
    <div class="page" style="padding:20px;height:700px;">
        <el-row>
            <el-card >
                 <div style="font-size: 20px;margin-bottom: 7px;">人员画像</div>
                 <!-- <span>人员画像，介绍xxxxx</span> -->
            </el-card>
        </el-row>

        <el-row :gutter="20" style="margin-top:20px;margin-bottom:20px;height:575px;">
            <el-col :span="6" :xs="24">
              <person-card :personInfo="personInfo" />
            </el-col>
    
            <el-col :span="18" :xs="24">
                <!--min-height:526px;  -->
              <el-card body-style="height:578px;">
                <el-tabs v-model="activeTab">
                    <el-tab-pane label="人员关系链" name="group">
                        <template slot="label">
                            <svg style="position: absolute;bottom:4;" t="1686316849629" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4401" data-spm-anchor-id="a313x.7781069.0.i55" width="30" height="30"><path d="M478.179556 350.449778c0 5.617778-0.156444 11.207111-0.867556 16.654222-6.016 56.647111-41.671111 104.789333-91.491556 127.729778-16.213333 7.694222-33.706667 12.444444-52.039111 14.264889-5.020444 0.440889-9.941333 0.725333-14.961778 0.725333-1.550222 0-3.100444 0-4.608-0.284444-23.665778-0.583111-45.767111-6.314667-65.621333-16.099556-12.302222-6.030222-23.637333-13.568-33.863111-22.371556-29.795556-25.756444-50.076444-62.407111-54.4-103.964444-0.554667-5.447111-0.853333-11.036444-0.853333-16.654222 0-30.336 8.248889-58.325333 22.784-82.375111 0.440889-0.711111 0.867556-1.393778 1.137778-1.962667 22.101333-35.541333 57.784889-61.411556 99.754667-71.068444 11.491556-2.517333 23.352889-3.911111 35.683556-3.911111 65.180444 0 121.287111 38.897778 145.777778 95.004444 0 0.128 0.270222 0.128 0.270222 0.398222C473.272889 305.976889 478.179556 327.651556 478.179556 350.449778zM411.576889 503.651556c-8.248889-3.370667-16.654222-6.442667-25.756444-8.817778-42.510222-11.335111-92.472889-11.889778-137.230222-1.408-11.192889 2.801778-22.371556 6.144-32.867556 10.225778-0.284444 0.128-0.725333 0.270222-0.995556 0.412444-23.352889 9.244444-44.643556 19.313778-63.772444 29.795556C43.363556 592.896 1.408 668.16 3.356444 729.031111c2.232889 71.921778 292.252444 69.390222 316.743111 69.532444 24.334222 0.298667 291.399111 1.664 292.792889-69.532444C610.929778 629.973333 468.508444 527.274667 411.576889 503.651556zM323.441778 745.528889l-62.947556-51.626667 53.731556-184.362667c1.507556 0.284444 3.057778 0.284444 4.608 0.284444 5.020444 0 9.941333-0.284444 14.961778-0.725333l45.184 185.784889L323.441778 745.528889zM474.168889 287.957333M497.777778 469.333333l213.333333 0 0 28.444444-213.333333 0 0-28.444444ZM682.666667 184.888889l28.444444 0 0 597.333333-28.444444 0 0-597.333333ZM682.666667 184.888889l241.777778 0 0 28.444444-241.777778 0 0-28.444444ZM696.888889 469.333333l227.555556 0 0 28.444444-227.555556 0 0-28.444444ZM682.666667 753.777778l241.777778 0 0 28.444444-241.777778 0 0-28.444444ZM977.777778 200.888889m-33.777778 0a2.375 2.375 0 1 0 67.555556 0 2.375 2.375 0 1 0-67.555556 0ZM977.777778 485.333333m-33.777778 0a2.375 2.375 0 1 0 67.555556 0 2.375 2.375 0 1 0-67.555556 0ZM977.777778 769.777778m-33.777778 0a2.375 2.375 0 1 0 67.555556 0 2.375 2.375 0 1 0-67.555556 0Z" fill="#AFB4FF" p-id="4402" data-spm-anchor-id="a313x.7781069.0.i51" class="selected"></path></svg> 
                            <span style="margin-left:34px;bottom:0;">人员关系链</span>
                        </template>
                        <!--  展示合作图谱？展示所在团伙情况，以及id，给予跳转到团伙详情的链接 -->
                        <div>
                            <div class="info-box mb-3 bg-warning" style="background-color: ;">
                                <span class="info-box-icon">
                                    <svg  width="40" height="40" t="1686318716189" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1504"><path d="M103.185067 510.634667c0 225.518933 182.784 408.302933 408.234666 408.302933 225.4848 0 408.2688-182.784 408.2688-408.2688S736.938667 102.4 511.453867 102.4C285.969067 102.4 103.185067 285.184 103.185067 510.634667z" fill="#85C2FF" p-id="1505"></path><path d="M605.7984 474.760533l-0.682667-1.570133c-0.1024-0.1024-0.1024-0.170667-0.2048-0.341333a35.6352 35.6352 0 1 0-63.3856 32.426666c9.898667 22.357333 5.563733 49.5616-12.6976 67.925334L433.186133 669.013333a60.928 60.928 0 0 1-86.084266 0 60.928 60.928 0 0 1 0-86.084266l35.6352-35.669334-0.238934-0.238933a35.601067 35.601067 0 1 0-49.5616-50.858667l-0.1024-0.1024-36.352 36.352a132.164267 132.164267 0 0 0 0 186.948267 132.164267 132.164267 0 0 0 186.948267 0l95.914667-95.914667a132.232533 132.232533 0 0 0 26.453333-148.6848z" fill="#FFFFFF" p-id="1506"></path><path d="M731.4432 292.317867a132.164267 132.164267 0 0 0-186.948267 0l-95.914666 95.914666a132.232533 132.232533 0 0 0-26.5216 148.616534l0.682666 1.536c0.1024 0.1024 0.1024 0.2048 0.170667 0.341333a35.6352 35.6352 0 1 0 63.3856-32.426667 61.303467 61.303467 0 0 1 12.6976-67.925333l95.744-95.709867a60.928 60.928 0 0 1 86.084267 0 60.928 60.928 0 0 1 0 86.084267l-35.6352 35.6352 0.238933 0.273067a35.601067 35.601067 0 1 0 49.595733 50.858666l0.068267 0.1024 36.352-36.352a132.3008 132.3008 0 0 0 0-186.948266z" fill="#FFFFFF" p-id="1507"></path></svg>
                                </span>
                                <div class="info-box-content">
                                    <span class="info-box-text">相关网站</span>
                                    <span class="info-box-number">{{labelCounts.Website==undefined?0:labelCounts.Website}}</span>
                                </div>
                            </div>

                            <div class="info-box mb-3 bg-warning" style="background-color: ;">
                                <span class="info-box-icon">
                                    <svg t="1686320874826" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3260" id="mx_n_1686320874827" width="40" height="40" data-spm-anchor-id="a313x.7781069.0.i57"><path d="M103.185067 510.634667c0 225.518933 182.784 408.302933 408.234666 408.302933 225.4848 0 408.2688-182.784 408.2688-408.2688S736.938667 102.4 511.453867 102.4C285.969067 102.4 103.185067 285.184 103.185067 510.634667z" fill="#9487DD" p-id="3261" data-spm-anchor-id="a313x.7781069.0.i50" class=""></path><path d="M605.7984 474.760533l-0.682667-1.570133c-0.1024-0.1024-0.1024-0.170667-0.2048-0.341333a35.6352 35.6352 0 1 0-63.3856 32.426666c9.898667 22.357333 5.563733 49.5616-12.6976 67.925334L433.186133 669.013333a60.928 60.928 0 0 1-86.084266 0 60.928 60.928 0 0 1 0-86.084266l35.6352-35.669334-0.238934-0.238933a35.601067 35.601067 0 1 0-49.5616-50.858667l-0.1024-0.1024-36.352 36.352a132.164267 132.164267 0 0 0 0 186.948267 132.164267 132.164267 0 0 0 186.948267 0l95.914667-95.914667a132.232533 132.232533 0 0 0 26.453333-148.6848z" fill="#e6e6e6" p-id="3262" data-spm-anchor-id="a313x.7781069.0.i51" class="selected"></path><path d="M731.4432 292.317867a132.164267 132.164267 0 0 0-186.948267 0l-95.914666 95.914666a132.232533 132.232533 0 0 0-26.5216 148.616534l0.682666 1.536c0.1024 0.1024 0.1024 0.2048 0.170667 0.341333a35.6352 35.6352 0 1 0 63.3856-32.426667 61.303467 61.303467 0 0 1 12.6976-67.925333l95.744-95.709867a60.928 60.928 0 0 1 86.084267 0 60.928 60.928 0 0 1 0 86.084267l-35.6352 35.6352 0.238933 0.273067a35.601067 35.601067 0 1 0 49.595733 50.858666l0.068267 0.1024 36.352-36.352a132.3008 132.3008 0 0 0 0-186.948266z" fill="#e6e6e6" p-id="3263" data-spm-anchor-id="a313x.7781069.0.i52" class="selected"></path></svg>
                                </span>
                                <div class="info-box-content">
                                    <span class="info-box-text">相关公司</span>
                                    <span class="info-box-number">{{labelCounts.Company==undefined?0:labelCounts.Company}}</span>
                                </div>
                            </div>

                            <div class="info-box mb-3 bg-warning" style="background-color: ;">
                                <span class="info-box-icon">
                                    <svg t="1686320874826" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3260" id="mx_n_1686320874827" width="40" height="40" data-spm-anchor-id="a313x.7781069.0.i57"><path d="M103.185067 510.634667c0 225.518933 182.784 408.302933 408.234666 408.302933 225.4848 0 408.2688-182.784 408.2688-408.2688S736.938667 102.4 511.453867 102.4C285.969067 102.4 103.185067 285.184 103.185067 510.634667z" fill="#dd6572" p-id="3261" data-spm-anchor-id="a313x.7781069.0.i50" class=""></path><path d="M605.7984 474.760533l-0.682667-1.570133c-0.1024-0.1024-0.1024-0.170667-0.2048-0.341333a35.6352 35.6352 0 1 0-63.3856 32.426666c9.898667 22.357333 5.563733 49.5616-12.6976 67.925334L433.186133 669.013333a60.928 60.928 0 0 1-86.084266 0 60.928 60.928 0 0 1 0-86.084266l35.6352-35.669334-0.238934-0.238933a35.601067 35.601067 0 1 0-49.5616-50.858667l-0.1024-0.1024-36.352 36.352a132.164267 132.164267 0 0 0 0 186.948267 132.164267 132.164267 0 0 0 186.948267 0l95.914667-95.914667a132.232533 132.232533 0 0 0 26.453333-148.6848z" fill="#dbdbdb" p-id="3262" data-spm-anchor-id="a313x.7781069.0.i51" class="selected"></path><path d="M731.4432 292.317867a132.164267 132.164267 0 0 0-186.948267 0l-95.914666 95.914666a132.232533 132.232533 0 0 0-26.5216 148.616534l0.682666 1.536c0.1024 0.1024 0.1024 0.2048 0.170667 0.341333a35.6352 35.6352 0 1 0 63.3856-32.426667 61.303467 61.303467 0 0 1 12.6976-67.925333l95.744-95.709867a60.928 60.928 0 0 1 86.084267 0 60.928 60.928 0 0 1 0 86.084267l-35.6352 35.6352 0.238933 0.273067a35.601067 35.601067 0 1 0 49.595733 50.858666l0.068267 0.1024 36.352-36.352a132.3008 132.3008 0 0 0 0-186.948266z" fill="#dbdbdb" p-id="3263" data-spm-anchor-id="a313x.7781069.0.i52" class="selected"></path></svg>
                                </span>
                                <div class="info-box-content">
                                    <span class="info-box-text">相关人员</span>
                                    <span class="info-box-number">{{labelCounts.Person==undefined?0:labelCounts.Person}}</span>
                                </div>
                            </div>
                            <div class="info-box mb-3 bg-warning" style="background-color: ;">
                                <span class="info-box-icon">
                                    <svg t="1686320874826" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3260" id="mx_n_1686320874827" width="40" height="40"><path d="M103.185067 510.634667c0 225.518933 182.784 408.302933 408.234666 408.302933 225.4848 0 408.2688-182.784 408.2688-408.2688S736.938667 102.4 511.453867 102.4C285.969067 102.4 103.185067 285.184 103.185067 510.634667z" fill="#9DD8C8" p-id="3261" data-spm-anchor-id="a313x.7781069.0.i50" class=""></path><path d="M605.7984 474.760533l-0.682667-1.570133c-0.1024-0.1024-0.1024-0.170667-0.2048-0.341333a35.6352 35.6352 0 1 0-63.3856 32.426666c9.898667 22.357333 5.563733 49.5616-12.6976 67.925334L433.186133 669.013333a60.928 60.928 0 0 1-86.084266 0 60.928 60.928 0 0 1 0-86.084266l35.6352-35.669334-0.238934-0.238933a35.601067 35.601067 0 1 0-49.5616-50.858667l-0.1024-0.1024-36.352 36.352a132.164267 132.164267 0 0 0 0 186.948267 132.164267 132.164267 0 0 0 186.948267 0l95.914667-95.914667a132.232533 132.232533 0 0 0 26.453333-148.6848z" fill="#e6e6e6" p-id="3262" data-spm-anchor-id="a313x.7781069.0.i51" class=""></path><path d="M731.4432 292.317867a132.164267 132.164267 0 0 0-186.948267 0l-95.914666 95.914666a132.232533 132.232533 0 0 0-26.5216 148.616534l0.682666 1.536c0.1024 0.1024 0.1024 0.2048 0.170667 0.341333a35.6352 35.6352 0 1 0 63.3856-32.426667 61.303467 61.303467 0 0 1 12.6976-67.925333l95.744-95.709867a60.928 60.928 0 0 1 86.084267 0 60.928 60.928 0 0 1 0 86.084267l-35.6352 35.6352 0.238933 0.273067a35.601067 35.601067 0 1 0 49.595733 50.858666l0.068267 0.1024 36.352-36.352a132.3008 132.3008 0 0 0 0-186.948266z" fill="#e6e6e6" p-id="3263" data-spm-anchor-id="a313x.7781069.0.i52" class=""></path></svg>
                                </span>
                                <div class="info-box-content">
                                    <span class="info-box-text">相关链接</span>
                                    <span class="info-box-number">{{labelCounts.Downlink==undefined?0:labelCounts.Downlink}}</span>
                                </div>
                            </div>
                            <div class="info-box mb-3 bg-warning" style="background-color: ;">
                                <span class="info-box-icon">
                                    <!-- <svg t="1686320874826" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3260" id="mx_n_1686320874827" width="40" height="40" data-spm-anchor-id="a313x.7781069.0.i57"><path d="M103.185067 510.634667c0 225.518933 182.784 408.302933 408.234666 408.302933 225.4848 0 408.2688-182.784 408.2688-408.2688S736.938667 102.4 511.453867 102.4C285.969067 102.4 103.185067 285.184 103.185067 510.634667z" fill="#FCE8AA" p-id="3261" data-spm-anchor-id="a313x.7781069.0.i50" class=""></path><path d="M605.7984 474.760533l-0.682667-1.570133c-0.1024-0.1024-0.1024-0.170667-0.2048-0.341333a35.6352 35.6352 0 1 0-63.3856 32.426666c9.898667 22.357333 5.563733 49.5616-12.6976 67.925334L433.186133 669.013333a60.928 60.928 0 0 1-86.084266 0 60.928 60.928 0 0 1 0-86.084266l35.6352-35.669334-0.238934-0.238933a35.601067 35.601067 0 1 0-49.5616-50.858667l-0.1024-0.1024-36.352 36.352a132.164267 132.164267 0 0 0 0 186.948267 132.164267 132.164267 0 0 0 186.948267 0l95.914667-95.914667a132.232533 132.232533 0 0 0 26.453333-148.6848z" fill="#cdcdcd" p-id="3262" data-spm-anchor-id="a313x.7781069.0.i51" class="selected"></path><path d="M731.4432 292.317867a132.164267 132.164267 0 0 0-186.948267 0l-95.914666 95.914666a132.232533 132.232533 0 0 0-26.5216 148.616534l0.682666 1.536c0.1024 0.1024 0.1024 0.2048 0.170667 0.341333a35.6352 35.6352 0 1 0 63.3856-32.426667 61.303467 61.303467 0 0 1 12.6976-67.925333l95.744-95.709867a60.928 60.928 0 0 1 86.084267 0 60.928 60.928 0 0 1 0 86.084267l-35.6352 35.6352 0.238933 0.273067a35.601067 35.601067 0 1 0 49.595733 50.858666l0.068267 0.1024 36.352-36.352a132.3008 132.3008 0 0 0 0-186.948266z" fill="#cdcdcd" p-id="3263" data-spm-anchor-id="a313x.7781069.0.i52" class="selected"></path></svg> -->
                                    <svg t="1686410568485" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3527" data-spm-anchor-id="a313x.7781069.0.i22" width="40" height="40"><path d="M103.185067 510.634667c0 225.518933 182.784 408.302933 408.234666 408.302933 225.4848 0 408.2688-182.784 408.2688-408.2688S736.938667 102.4 511.453867 102.4C285.969067 102.4 103.185067 285.184 103.185067 510.634667z" fill="#FFD95A" p-id="3528" data-spm-anchor-id="a313x.7781069.0.i18" class=""></path><path d="M605.7984 474.760533l-0.682667-1.570133c-0.1024-0.1024-0.1024-0.170667-0.2048-0.341333a35.6352 35.6352 0 1 0-63.3856 32.426666c9.898667 22.357333 5.563733 49.5616-12.6976 67.925334L433.186133 669.013333a60.928 60.928 0 0 1-86.084266 0 60.928 60.928 0 0 1 0-86.084266l35.6352-35.669334-0.238934-0.238933a35.601067 35.601067 0 1 0-49.5616-50.858667l-0.1024-0.1024-36.352 36.352a132.164267 132.164267 0 0 0 0 186.948267 132.164267 132.164267 0 0 0 186.948267 0l95.914667-95.914667a132.232533 132.232533 0 0 0 26.453333-148.6848z" fill="#bfbfbf" p-id="3529" data-spm-anchor-id="a313x.7781069.0.i19" class=""></path><path d="M731.4432 292.317867a132.164267 132.164267 0 0 0-186.948267 0l-95.914666 95.914666a132.232533 132.232533 0 0 0-26.5216 148.616534l0.682666 1.536c0.1024 0.1024 0.1024 0.2048 0.170667 0.341333a35.6352 35.6352 0 1 0 63.3856-32.426667 61.303467 61.303467 0 0 1 12.6976-67.925333l95.744-95.709867a60.928 60.928 0 0 1 86.084267 0 60.928 60.928 0 0 1 0 86.084267l-35.6352 35.6352 0.238933 0.273067a35.601067 35.601067 0 1 0 49.595733 50.858666l0.068267 0.1024 36.352-36.352a132.3008 132.3008 0 0 0 0-186.948266z" fill="#bfbfbf" p-id="3530" data-spm-anchor-id="a313x.7781069.0.i20" class=""></path></svg>    
                                </span>
                                <div class="info-box-content">
                                    <span class="info-box-text">相关IP</span>
                                    <span class="info-box-number">{{labelCounts.Ip==undefined?0:labelCounts.Ip}}</span>
                                </div>
                            </div>
                        </div>
                        <div id="person-graph" style=""></div>
                    </el-tab-pane>
                    <!-- <el-tab-pane v-if="personInfo.companyList!=null" label="旗下公司" name="company">
                        <div style="">
                        <el-descriptions class="margin-top" :column="2" size="medium" border>
                            <template slot="title" >
                                <i class=" el-icon-user-solid" style="color:#C6C8C0" ></i> 
                                <span style="color:#C6C8C0">公司溯源</span>
                            </template>
                        <el-descriptions-item label="主办单位名">
                            <div class="null-text" v-if="personInfo.companyList[0].companyName==null">暂无</div>
                            <div v-else>{{personInfo.companyList[0].companyName}}</div>
                        </el-descriptions-item>
                        <el-descriptions-item label="单位性质">
                            <div class="null-text" v-if="personInfo.companyList[0].companyType==null">暂无</div>
                            <div v-else>{{personInfo.companyList[0].companyType}}</div>
                        </el-descriptions-item>
                        <el-descriptions-item>
                            <template slot="label">
                            法定代表人
                            </template>
                            <div class="null-text" v-if="personInfo.personName==null">暂无</div>
                            <el-tag v-else size="small" type="plain" style="border-color:purple;color: purple;">{{personInfo.personName}}</el-tag>
                        </el-descriptions-item>
                        
                        <el-descriptions-item>
                            <template slot="label">
                            注册资本
                            </template>
                            <div class="null-text" v-if="personInfo.companyList[0].registerCapital==null">暂无</div>
                            <div v-else>{{personInfo.companyList[0].registerCapital}}</div>
                        </el-descriptions-item>
                
                        <el-descriptions-item>
                            <template slot="label">
                            注册时间
                            </template>
                            <div class="null-text" v-if="personInfo.companyList[0].registerTime==null">暂无</div>
                            <el-tag v-else size="small" type="plain" style="border-color:purple;color: purple;">{{personInfo.companyList[0].registerTime}}</el-tag>
                        </el-descriptions-item>
                
                        <el-descriptions-item>
                            <template slot="label">
                            公司状态
                            </template>
                            <div class="null-text" v-if="personInfo.companyList[0].companyStatus==null">暂无</div>
                            <div v-else>{{personInfo.companyList[0].companyStatus}}</div>
                        </el-descriptions-item>
                        <el-descriptions-item>
                            <template slot="label">
                                公司类型
                            </template>
                            <div class="null-text" v-if="personInfo.companyList[0].companyType==null">暂无</div>
                            <div v-else>{{personInfo.companyList[0].companyType}}</div>
                        </el-descriptions-item>
                        <el-descriptions-item>
                            <template slot="label">
                                工商注册号
                            </template>
                            <div class="null-text" v-if="personInfo.companyList[0].registerNumber==null">暂无</div>
                            <div v-else>{{personInfo.companyList[0].registerNumber}}</div>
                        </el-descriptions-item>
                        <el-descriptions-item>
                        <template slot="label">
                            所属行业
                        </template>
                        <div class="null-text" v-if="personInfo.companyList[0].industry==null">暂无</div>
                        <div v-else>{{personInfo.companyList[0].industry}}</div>
                        </el-descriptions-item>
                        <el-descriptions-item>
                            <template slot="label">
                                核准日期
                            </template>
                            <div class="null-text" v-if="personInfo.companyList[0].approvalDate==null">暂无</div>
                            <div v-else>{{personInfo.companyList[0].approvalDate}}</div>
                        </el-descriptions-item>
                        <el-descriptions-item>
                            <template slot="label">
                                注册地址
                            </template>
                            <div class="null-text" v-if="personInfo.companyList[0].registerAddress==null">暂无</div>
                            <div v-else>{{personInfo.companyList[0].registerAddress}}</div>
                        </el-descriptions-item>
                
                        <el-descriptions-item>
                            <template slot="label">
                                经营范围
                            </template>
                            <div style="height:40px;overflow: hidden; /* 隐藏超出部分 */
                            text-overflow: ellipsis; /* 以省略号显示超出部分 */
                            white-space: nowrap; /* 不换行 */">
                                <div class="null-text" v-if="personInfo.companyList[0].businessScope==null">暂无</div>
                                <div v-else style="height:60px">{{personInfo.companyList[0].businessScope}}</div>

                            </div>
                            
                        </el-descriptions-item>
                
                        </el-descriptions>
                        </div>     
                    </el-tab-pane> -->
                    <el-tab-pane label="旗下资产" name="website">
                        <template slot="label">
                            <svg style="position: absolute;bottom:4;" t="1686317217411" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4988" width="31" height="31"><path d="M636.416 598.016c-17.408 0-33.792 6.656-45.568 17.92l-165.376-96.256c1.024-5.12 2.048-10.752 2.048-16.384s-1.024-11.264-2.048-16.384l163.84-95.744c12.288 11.776 29.184 18.944 47.104 18.944 38.4 0 69.632-31.232 69.632-69.632s-31.232-69.632-69.632-69.632-69.632 31.232-69.632 69.632c0 5.632 1.024 11.264 2.048 16.384l-163.84 95.744c-12.288-11.776-29.184-18.944-47.104-18.944-38.4 0-69.632 31.232-69.632 69.632s31.232 69.632 69.632 69.632c18.432 0 34.816-7.168 47.104-18.944l165.376 96.256c-1.024 5.12-2.048 9.728-2.048 15.36 0 37.376 30.208 67.584 67.584 67.584 37.376 0 67.584-30.208 67.584-67.584 0.512-37.376-29.696-67.584-67.072-67.584z" fill="#DCCBFF" p-id="4989"></path><path d="M729.088 655.872c-17.408 0-33.792 6.656-45.568 17.92l-165.376-96.256c1.024-5.12 2.048-10.752 2.048-16.384s-1.024-11.264-2.048-16.384l163.84-95.744c12.288 11.776 29.184 18.944 47.104 18.944 38.4 0 69.632-31.232 69.632-69.632s-31.232-69.632-69.632-69.632-69.632 31.232-69.632 69.632c0 5.632 1.024 11.264 2.048 16.384l-163.84 95.744C485.888 498.688 468.992 491.52 450.56 491.52c-38.4 0-69.632 31.232-69.632 69.632s31.232 69.632 69.632 69.632c18.432 0 34.816-7.168 47.104-18.944l165.376 96.256c-1.024 5.12-2.048 9.728-2.048 15.36 0 37.376 30.208 67.584 67.584 67.584 37.376 0 67.584-30.208 67.584-67.584s-29.696-67.584-67.072-67.584z" fill="#A87DFF" p-id="4990"></path><path d="M276.992 331.264h-29.696v-29.696c0-6.656-5.12-11.776-11.776-11.776-6.656 0-11.776 5.12-11.776 11.776v29.696H194.56c-6.656 0-11.776 5.12-11.776 11.776s5.12 11.776 11.776 11.776h29.696V384c0 6.656 5.12 11.776 11.776 11.776 6.656 0 11.776-5.12 11.776-11.776v-29.696h29.696c6.656 0 11.776-5.12 11.776-11.776s-6.144-11.264-12.288-11.264zM278.016 698.368c20.48 0 30.72 16.384 38.4 28.672 7.68 12.288 11.264 17.408 18.432 17.408 6.656 0 10.752-5.12 18.432-17.408 7.168-12.288 17.408-28.672 38.4-28.672 20.48 0 30.72 16.384 38.4 28.672 7.68 12.288 11.264 17.408 18.432 17.408 6.656 0 11.776 5.12 11.776 11.776 0 6.656-5.12 11.776-11.776 11.776-20.48 0-30.72-16.384-38.4-28.672-7.68-12.288-11.264-17.408-18.432-17.408-6.656 0-10.752 5.12-18.432 17.408-7.168 12.288-17.408 28.672-38.4 28.672-20.48 0-30.72-16.384-38.4-28.672-7.68-12.288-11.264-17.408-18.432-17.408s-10.752 5.632-18.432 17.408c-7.168 12.288-17.408 28.672-38.4 28.672-6.656 0-11.776-5.12-11.776-11.776 0-6.656 5.12-11.776 11.776-11.776 7.168 0 10.752-5.12 18.432-17.408 7.68-11.776 17.92-28.672 38.4-28.672z" fill="#EAB3FF" p-id="4991"></path><path d="M833.536 496.64h65.536v65.536h-65.536z" fill="#F7E2FF" p-id="4992"></path><path d="M157.184 575.488m-32.768 0a32.768 32.768 0 1 0 65.536 0 32.768 32.768 0 1 0-65.536 0Z" fill="#F7E2FF" p-id="4993"></path></svg>
                            <span style="margin-left:34px;bottom:0;">旗下资产</span>
                        </template>
                        <div style="margin-top:20px;">
                            <el-descriptions :column="3" size="medium" v-if="personInfo.companyList!=null">
                                <template slot="title" >
                                    <i class=" el-icon-user-solid" style="color:#D0B8FE" ></i> 
                                    <span style="color:#D0B8FE"> 公司溯源</span>
                                </template>
                            <el-descriptions-item label="公司名称">
                                <div class="null-text" v-if="personInfo.companyList[0].companyName==null">暂无</div>
                                <div v-else><a-tag  color="#654E92">{{personInfo.companyList[0].companyName}}</a-tag></div>
                            </el-descriptions-item>
                            <el-descriptions-item label="单位性质">
                                <div class="null-text" v-if="personInfo.companyList[0].companyType==null">暂无</div>
                                <div v-else>{{personInfo.companyList[0].companyType}}</div>
                            </el-descriptions-item>
                            <el-descriptions-item>
                                <template slot="label">
                                注册资本
                                </template>
                                <div class="null-text" v-if="personInfo.companyList[0].registerCapital==null">暂无</div>
                                <div v-else>{{personInfo.companyList[0].registerCapital}}</div>
                            </el-descriptions-item>
                    
                            <el-descriptions-item>
                                <template slot="label">
                                注册时间
                                </template>
                                <div class="null-text" v-if="personInfo.companyList[0].registerTime==null">暂无</div>
                                {{personInfo.companyList[0].registerTime}}
                            </el-descriptions-item>
                    
                            <el-descriptions-item>
                                <template slot="label">
                                公司状态
                                </template>
                                <div class="null-text" v-if="personInfo.companyList[0].companyStatus==null">暂无</div>
                                <div v-else>{{personInfo.companyList[0].companyStatus}}</div>
                            </el-descriptions-item>
                            <el-descriptions-item>
                                <template slot="label">
                                    公司类型
                                </template>
                                <div class="null-text" v-if="personInfo.companyList[0].companyType==null">暂无</div>
                                <div v-else>{{personInfo.companyList[0].companyType}}</div>
                            </el-descriptions-item>
                            <el-descriptions-item>
                                <template slot="label">
                                    工商注册号
                                </template>
                                <div class="null-text" v-if="personInfo.companyList[0].registerNumber==null">暂无</div>
                                <div v-else>{{personInfo.companyList[0].registerNumber}}</div>
                            </el-descriptions-item>
                            <el-descriptions-item>
                            <template slot="label">
                                所属行业
                            </template>
                            <div class="null-text" v-if="personInfo.companyList[0].industry==null">暂无</div>
                            <div v-else>{{personInfo.companyList[0].industry}}</div>
                            </el-descriptions-item>
                            <el-descriptions-item>
                                <template slot="label">
                                    核准日期
                                </template>
                                <div class="null-text" v-if="personInfo.companyList[0].approvalDate==null">暂无</div>
                                <div v-else>{{personInfo.companyList[0].approvalDate}}</div>
                            </el-descriptions-item>
                            <el-descriptions-item>
                                <template slot="label">
                                    注册地址
                                </template>
                                <div class="null-text" v-if="personInfo.companyList[0].registerAddress==null">暂无</div>
                                <div v-else>{{personInfo.companyList[0].registerAddress}}</div>
                            </el-descriptions-item>
                    
                            <!-- <el-descriptions-item>
                                <template slot="label">
                                    经营范围
                                </template>
                                <div style="height:80px;overflow: hidden; /* 隐藏超出部分 */
                                text-overflow: ellipsis; /* 以省略号显示超出部分 */
                                white-space: nowrap; /* 不换行 */">
                                    <div class="null-text" v-if="personInfo.companyList[0].businessScope==null">暂无</div>
                                    <div v-else style="height:60px">{{personInfo.companyList[0].businessScope}}</div>
    
                                </div>
                                
                            </el-descriptions-item> -->
                    
                            </el-descriptions>

                            <div style="margin-top:20px;">
                                <i class="el-icon-star-on" style="color:#D0B8FE" ></i> 
                                <span style="color:#D0B8FE;font-size: 16px;font-weight: bold;"> 旗下网站</span>
                                <div style="margin-top:20px;"  v-if="personInfo.companyList!=null && personInfo.companyList[0].siteList!=null"> 
                                    <el-descriptions v-for="(item,index) in personInfo.companyList[0].siteList" :key="index"   :column="3" size="medium">
                                        <el-descriptions-item label="URL">
                                            <div><a-tag  color="#654E92">{{item.url}}</a-tag></div>
                                            <a-tag v-if="item.isMalicious==true" color="rgb(166 13 13)">恶意网站</a-tag>
                                            <a-tag v-else color="green">正常网站</a-tag>
                                        </el-descriptions-item>
                                        <el-descriptions-item label="网站ip">
                                            <div>{{item.ip}}</div>
                                        </el-descriptions-item>
                                        <el-descriptions-item label="网站标题">
                                            <div>{{item.siteTitle}}</div>
                                        </el-descriptions-item>
                                    </el-descriptions>
                                </div>
                            </div>
                        </div>
                    </el-tab-pane>
                    <el-tab-pane label="" name="timeline">
                        <template slot="label">
                            <svg style="position: absolute;bottom:7;"  width="20" height="20" t="1686318208640" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2292"><path d="M1024 628.363636v279.272728H372.363636V628.363636h651.636364z m-69.818182 69.818182H442.181818v139.636364h512v-139.636364z m69.818182-581.818182v279.272728H372.363636V116.363636h651.636364z m-69.818182 69.818182H442.181818v139.636364h512V186.181818z" fill="#B1B2FF" p-id="2293" data-spm-anchor-id="a313x.7781069.0.i13" class="selected"></path><path d="M139.636364 395.636364A139.636364 139.636364 0 1 1 139.636364 116.363636a139.636364 139.636364 0 0 1 0 279.272728z m0 232.727272a139.636364 139.636364 0 1 1 0 279.272728 139.636364 139.636364 0 0 1 0-279.272728z" fill="#B1B2FF" p-id="2294" data-spm-anchor-id="a313x.7781069.0.i11" class="selected"></path><path d="M116.363636 395.636364h46.545455v232.727272H116.363636z" fill="#B1B2FF" p-id="2295" data-spm-anchor-id="a313x.7781069.0.i12" class="selected"></path></svg>
                            <span style="margin-left:28px;bottom:0;">行为动态</span>
                        </template>
                        <timeline />
                    </el-tab-pane>
                </el-tabs>
              </el-card>
            </el-col>
    
          </el-row>
    </div>
</template>

<script>
import PersonCard from './component/PersonCard.vue';
import Timeline from './component/Timeline.vue';
import CompanyInfoCard from '@/views/malwaresites/detail/component/CompanyInfoCard.vue';
import G6 from '@antv/g6';
import insertCss from 'insert-css';

export default {
    data() {
        return {
            text: `A dog is a type of domesticated animal.Known for its loyalty and faithfulness,it can be found as a welcome guest in many households across the world.`,
            activeTab: 'group',
            personInfo:'',
            pid:'',
            graph:'',
            graphCanvas:'',
            labelType:{
                "Website":"网站",
                "Company":"公司",
                "Person":"人员",
                "Ip":"IP",
                "Downlink":"下载链接",
            },
            labelCounts:'',
        }
    },
    components:{
        PersonCard,
        Timeline,
        CompanyInfoCard,
    },
    watch: {
        activeTab(key) {
          console.log(key);
          if(key=="group"){
            // this.showGraph()
          }
        },
    },
    created(){
        this.pid= this.$route.query.id;
        this.getPersonInfo();
    },
    methods: {
        getPersonInfo(){
            this.axios({
                url:"api/person/all/id/"+this.pid,
                method:'get'
            }).then(res=>{
                this.personInfo = res.data;
                console.log(this.personInfo);
                this.showGraph();
            })
        },
        countGraphType(){
            this.labelCounts = this.graph.nodes.reduce((acc, obj) => {
                const label = obj.label;
                acc[label] = (acc[label] || 0) + 1;
                return acc;
            }, {});
            console.log(this.labelCounts);
        },
        showGraph(depth=2){ //传入深度，默认为2度关系
            const containerId = "person-graph"
            const container = document.getElementById(containerId);
            const width = container.scrollWidth ||300;
            const height = container.scrollHeight || 385; //TODO:原本为420，这里修改画布的高度
            const canvasBackgroundColor = '#363B40';
            const darkBackColor = '#363B40'; //TODO:这里修改节点的背景颜色 原本rgb(43, 47, 51)
            container.style.backgroundColor = canvasBackgroundColor; //TODO:背景颜色?
            const nodeSize = 25;
            const nodeIconSize = 25;
            const realEdgeOpacity = 0.4;
            // box-shadow: rgb(174, 174, 174) 0px 0px 10px; padding: 0px 10px 24px 10px;
            insertCss(`
            .g6-component-tooltip {
                background-color: #363b40; 
                padding: 0px 20px 0px 20px;
                border-radius: 6px;
                color: hsla(0,0%,100%,.85);
                transition: opacity .2s;
                box-shadow: 0 5px 18px 0 rgba(0, 0, 0, 0.6);
                border: 0px;
            }
            .g6-component-tooltip li {
                cursor: pointer;
                list-style-type: none;
                list-style: none;
                margin-left: 0;
                line-height: 38px;
            }
            .g6-component-contextmenu {
                position: absolute;
                z-index: 2;
                list-style-type: none;
                background-color: #363b40; 
                border-radius: 6px;
                font-size: 14px;
                color: hsla(0,0%,100%,.85);
                width: fit-content;
                transition: opacity .2s;
                text-align: center;
                padding: 0px 20px 0px 20px;
                    box-shadow: 0 5px 18px 0 rgba(0, 0, 0, 0.6);
                    border: 0px;
            }
            .g6-component-contextmenu ul {
                    padding-left: 0px;
                    margin: 0;
            }
            .g6-component-contextmenu li {
                cursor: pointer;
                list-style-type: none;
                list-style: none;
                margin-left: 0;
                line-height: 38px;
            }
            .g6-component-contextmenu li:hover {
                color: #aaaaaa;
                }
            .g6-component-toolbar li {
                list-style-type: none !important;
            }
            `);
            ////https://gw.alipayobjects.com/os/antvdemo/assets/data/relations.json
            ///TODO:现在数据库还没建立起来，所以无法通过域名名称查到对应的图谱。
            //api/graph/domain?dname=example.com1&depth=2
            //真正的请求'api/graph/domain?'+"dname="+this.siteInfo.domain+"&depth="+depth
            //测试请求api/graph/test 最初的测试api，数据写死    http://localhost:8888/graph/test
            fetch('api/graph/person?'+"pname="+this.personInfo.personName+"&depth="+depth) 
            .then((res) => res.json())
            .then((data) => {
                //TODO:调用图谱统计方法
                this.graph = data;
                console.log(this.graph)
                this.countGraphType();
                const subjectColors = [
                    '#5F95FF', // blue
                    '#61DDAA',
                    // '#65789B',
                    '#F6BD16',
                    '#9661BC', //purple
                    '#C9CCD5', //blue
                    // '#9661BC',
                    '#F6903D',
                    '#008685',
                    '#F08BB4',
                ];
                const backColor = '#fff';//
                const theme = 'default';
                const disableColor = '#777';
                const colorSets = G6.Util.getColorSetsBySubjectColors(
                    subjectColors,
                    backColor,
                    theme,
                    disableColor,
                );

                // //1、PageRank算法结果展示
                // let result = pageRank(data); //return Object[id: pagerank] 
                // this.showPageRankColumn(result);
                // console.log(result);
                // //2、桑基图
                // this.showSanky(data.edges);

                //3、分类
                const clusterNode = ["Website","Company","Person","Ip","Downlink"];
                const clusterEdge = ["BELONGS_TO","DOWN_FROM","HAS_IP","HAS_COMPANY","SIMILAR_TO","CONNECT"];
                // const clusterNode = ["Domain","Company","Person","Ip","Cert"];
                data.nodes.forEach(function (node) {
                    const cid = clusterNode.indexOf(node.label);
                    node.legendType=node.label;
                    if (!node.style) {
                        node.style = {};
                    }
                    node.icon = {
                        show:true,
                        img:require("@/assets/nodes/"+node.label+".png"),
                    };
                    if(node.label=="Website"){
                        if(node.properties["Is_bad"]==true){
                            node.icon.img = require("@/assets/nodes/Malsite.png");
                        }
                    }
                    node.style.fill = darkBackColor;   //colorSets[cid].mainStroke; 
                    node.style.stroke = darkBackColor;//colorSets[cid].mainStroke; 
                });
                
                // const clusterEdge = ["IS_SUB","FOUNDED_BY","HAS_IP","WORKS_FOR","HAS_CERT"];
                data.edges.forEach(edge => {
                    const cid = clusterEdge.indexOf(edge.label);
                    edge.legendType=edge.label;
                    edge.style = {
                        stroke: colorSets[cid].mainStroke,
                        endArrow:{
                            path: G6.Arrow.triangle(),
                            fill:colorSets[cid].mainStroke,
                        },
                    };
                    edge.color = colorSets[cid].mainStroke;  //设置边的颜色
                    edge.labelCfg={
                        autoRotate: true,
                        style: {
                            lineWidth: 4,
                            fill: colorSets[cid].mainStroke, //colorSets[i].mainStroke, //'#1890ff',  //文字颜色
                            fontSize: 12, //标签文字大小：原来14px
                            background: {
                                fill: "#2B384E",//colorSets[cid].mainFill, //标签背景颜色
                                stroke: colorSets[cid].mainStroke,  //colorSets[cid].mainStroke 标签边框
                                padding: [2, 2, 2, 2],
                                radius: 2,
                            },
                        },
                    };
                })

                var legendConfig = {}; 
                const nodeLegendSize = 15;
                var legendData = {}
                legendData.nodes = [];
                legendData.edges = [];
                var filterFunctions = {};
                clusterNode.forEach(element => {
                    const cid = clusterNode.indexOf(element);
                    var nodeLegendConfig = {};
                    nodeLegendConfig["r"]=nodeLegendSize; //图例节点的大小
                    nodeLegendConfig["style"] = {
                        "fill":colorSets[cid].mainStroke,
                        "stroke":colorSets[cid].mainStroke //设置这个，不然node的边框会变成蓝色
                    };
                    legendConfig[element]=nodeLegendConfig;

                    legendData.nodes.push({
                        id:element,
                        label:element,
                        ...legendConfig[element]
                    })
                    filterFunctions[element] = (d)=>{if (d.legendType === element) return true;return false}
                });

                clusterEdge.forEach(element=>{
                    const cid = clusterEdge.indexOf(element);
                    var edgeLegendConfig = {};
                    edgeLegendConfig["type"]="line"; //图例节点的大小
                    edgeLegendConfig["style"]={"stroke":colorSets[cid].mainStroke,"width":20};
                    legendConfig[element]=edgeLegendConfig;

                    legendData.edges.push({
                        id: element,
                        label: element,
                        ...legendConfig[element]
                    })
                    filterFunctions[element] = (d)=>{if (d.legendType === element) return true;return false}
                })
                console.log(filterFunctions)
                const legend = new G6.Legend({
                    data: legendData,
                    align: 'center',
                    layout: 'vertical', // vertical  图标水平或竖直  horizontal
                    position: 'bottom-left',  //TODO: 图标的位置原本为bottom-left
                    vertiSep: 10, //12竖直间距
                    horiSep: 20, //图例间的水平间距
                    offsetX: 10, //图例区域离 position 对应的默认位置的 x 方向的偏移量，可被用于图例位置的微调
                    offsetY: -10,
                    padding: [12, 4, 8, 16], //图例区域内部内容到边框的距离，四位数组分别代表上、右、下、左边距
                    containerStyle: {
                        fill: '#ccc',
                        lineWidth: 1
                    },
                    title: '',
                    titleConfig: {
                        position: 'center',
                        offsetX: 0,
                        offsetY: 12,
                    },
                    filter: {
                        enable: true,
                        trigger: 'mouseenter',
                        graphActiveState: 'activeByLegend',
                        graphInactiveState: 'inactiveByLegend',
                        filterFunctions: filterFunctions
                    }
                });

                //tooltip 悬浮提示框
                const tooltip = new G6.Tooltip({
                    offsetX: 10,
                    offsetY: 10,
                    // the types of items that allow the tooltip show up
                    // 允许出现 tooltip 的 item 类型
                    itemTypes: ['node', 'edge'],
                    // custom the tooltip's content
                    // 自定义 tooltip 内容
                    getContent: (e) => {
                        const outDiv = document.createElement('div');
                        outDiv.style.width = 'fit-content';
                        //outDiv.style.padding = '0px 0px 20px 0px';
                        if(e.item.getType()=="node"){
                            outDiv.innerHTML = `
                                <li>${this.labelType[e.item.getModel().label]}名称: ${e.item.getModel().properties["name"] || e.item.getModel().id}</li>
                            `;
                            return outDiv;
                        }
                        // else if(e.item.getType()=="edge"){
                        //     outDiv.innerHTML = `
                        //         <h4>边信息</h4>
                        //         <ul>
                                    
                        //             <li>边类型:<button style="font-weight: bold;"> ${e.item.getModel().label}</button></li>
                        //         </ul>
                        //     `;
                        // }
                        // return outDiv;
                    },
                });
                let hiddenItemIds = []; // 隐藏的元素 id 数组
                let expandArray = [];
                let collapseArray = [];
                let newAddArray = [];
                const hideItems = (graph) => {
                    hiddenItemIds.forEach((id) => {
                        graph.hideItem(id);
                    });
                };

                const showItems = (graph) => {
                    graph.getNodes().forEach((node) => {
                        if (!node.isVisible()) graph.showItem(node);
                    });
                    graph.getEdges().forEach((edge) => {
                        if (!edge.isVisible()) edge.showItem(edge);
                    });
                    hiddenItemIds = [];
                };

                const findNeighbors = (graph,model,depth=1) =>{
                    fetch("api/graph/domain?dname="+model.properties.name+"&depth="+depth)
                    .then((res) => res.json())
                    .then((data) => {
                        var newNodeCount = 0;
                        var newEdgeCount = 0;
                        data.nodes.forEach((node)=>{
                            if(!graph.findById(node.id)){
                                newNodeCount+=1;
                                newAddArray.push(node.id);
                                console.log("not find",node.id)
                                node.legendType=node.label;
                                if (!node.style) {
                                    node.style = {};
                                }
                                node.icon = {
                                    show:true,
                                    img:require("@/assets/nodes/"+node.label+".png"),
                                    // img:require("@/assets/nodes/Redirect.png"),
                                }
                                node.style.fill = "#2B384E";   //colorSets[cid].mainStroke; 
                                node.style.stroke = "#2B384E";
                                graph.addItem('node',node );
                            }
                        })

                        data.edges.forEach((edge)=>{
                            // edge.label=null;
                            const rs = graph.find("edge",(oedge)=>{
                                return oedge.get('model').source==edge.source&& oedge.get('model').target==edge.target;
                            })
                            console.log(rs)
                            if(!rs){
                                const cid = clusterEdge.indexOf(edge.label);
                                edge.legendType=edge.label;
                                edge.style = {
                                    stroke: colorSets[cid].mainStroke,
                                    endArrow:{
                                        path: G6.Arrow.triangle(),
                                        fill:colorSets[cid].mainStroke,
                                    },
                                };
                                edge.color = colorSets[cid].mainStroke;  //设置边的颜色
                                edge.labelCfg={
                                    autoRotate: true,
                                    style: {
                                        lineWidth: 4,
                                        fill: colorSets[cid].mainStroke, //colorSets[i].mainStroke, //'#1890ff',  //文字颜色
                                        fontSize: 12, //标签文字大小：原来14px
                                        background: {
                                            fill: "#2B384E",//colorSets[cid].mainFill, //标签背景颜色
                                            stroke: colorSets[cid].mainStroke,  //colorSets[cid].mainStroke 标签边框
                                            padding: [2, 2, 2, 2],
                                            radius: 2,
                                        },
                                    },
                                };
                                edge.id = 'edge' + edge.id;
                                graph.addItem('edge',edge );
                                newEdgeCount+=1;
                            }
                        })
                        if(newNodeCount==0){
                            this.noMoreInfo()
                        }else{
                            this.haveMoreInfo(newNodeCount,newEdgeCount)
                        }
                    })
                }
                //菜单 
                const contextMenu = new G6.Menu({
                    shouldBegin(evt) {
                        if (evt.target && evt.target.isCanvas && evt.target.isCanvas()) return true;
                        if (evt.item) return true;
                        return false;
                    },
                    getContent(evt) {
                        const { item } = evt;
                        let header;
                        // if (evt.target && evt.target.isCanvas && evt.target.isCanvas()) { //右键画布
                        //     return `<ul>
                        //     <li id='show'>显示全部隐藏节点</li>
                        //     <li id='collapseAll'>Collapse all Clusters</li>
                        //     </ul>`;
                        // } 
                        // else if (!item) return;
                        const itemType = item.getType();
                        const model = item.getModel();
                        if (itemType && model) {
                            if (itemType == 'node') { //右键节点
                                return `
                                    <ul>
                                        <li id='expand'>展开一度关联节点</li>
                                        <li id='expand2'>展开二度关联节点</li>
                                        <li id='hideNeighbor'>折叠关联节点</li>
                                        <li id='hide'>隐藏节点</li>
                                    </ul>`;
                            }
                        }
                    },
                    handleMenuClick: (target, item) => {
                        const model = item && item.getModel();
                        const liIdStrs = target.id.split('-');
                        let mixedGraphData;
                        switch (liIdStrs[0]) {
                        case 'hide':
                            graph.hideItem(item);
                            hiddenItemIds.push(model.id);
                            break;
                        case 'expand':
                            findNeighbors(graph,model)
                            break;
                        case 'expand2':
                            findNeighbors(graph,model,2)
                                break;
                        case 'collapse':
                            const aggregatedNode = aggregatedNodeMap[model.clusterId];
                            manipulatePosition = { x: aggregatedNode.x, y: aggregatedNode.y };
                            collapseArray.push(aggregatedNode);
                            for (let i = 0; i < expandArray.length; i++) {
                                if (expandArray[i].id === model.clusterId) {
                                    expandArray.splice(i, 1);
                                    break;
                                }
                            }
                            mixedGraphData = getMixedGraph(
                                clusteredData,
                                data,
                                nodeMap,
                                aggregatedNodeMap,
                                expandArray,
                                collapseArray,
                            );
                            break;
                        case 'collapseAll':
                            newAddArray.forEach(id=>{
                                graph.hideItem(id)
                            });
                            break;
                        case 'neighbor':
                            const expandNeighborSteps = parseInt(liIdStrs[1]);
                            mixedGraphData = getNeighborMixedGraph(
                                model,
                                expandNeighborSteps,
                                data,
                                clusteredData,
                                currentUnproccessedData,
                                nodeMap,
                                aggregatedNodeMap,
                                10,
                            );
                            break;
                        case 'hideNeighbor':
                            const node = graph.findById(model.id);
                            const neightborList = node.getNeighbors()
                            neightborList.forEach(element=>{
                                const id = element.getModel().id
                                graph.hideItem(id)
                                hiddenItemIds.push(id); //将邻居节点id加入隐藏数组
                            })
                            //隐藏节点本身
                            graph.hideItem(item);
                            hiddenItemIds.push(model.id);
                            break;
                        case 'show':
                            showItems(graph);
                            break;
                        default:
                            break;
                        }
                        if (mixedGraphData) {
                            cachePositions = cacheNodePositions(graph.getNodes());
                            currentUnproccessedData = mixedGraphData;
                            handleRefreshGraph(
                                graph,
                                currentUnproccessedData,
                                CANVAS_WIDTH,
                                CANVAS_HEIGHT,
                                largeGraphMode,
                                true,
                                false,
                            );
                        }
                },
                    // offsetX and offsetY include the padding of the parent container
                    // 需要加上父级容器的 padding-left 16 与自身偏移量 10
                    offsetX: 16 + 10,
                    // 需要加上父级容器的 padding-top 24 、画布兄弟元素高度、与自身偏移量 10
                    offsetY: 0,
                    // the types of items that allow the menu show up
                    // 在哪些类型的元素上响应
                    itemTypes: ['node', 'edge', 'canvas'],
                });
                //工具栏
                const toolbar = new G6.ToolBar({
                    position: { x: 10, y: 10 },
                });

                const graph = new G6.Graph({
                    container: containerId,
                    width,   //: 800,
                    height,//: 500,
                    // fitView:true, 别开最好
                    //TODO:注意 fitCenter和layout中的center只选择一个
                    // fitCenter: true,
                    modes: {
                        default: ['drag-canvas', 'activate-relations', 'zoom-canvas'],
                    },
                    
                    layout: {
                        type: 'force',
                        linkDistance: 180, //边的长度 180
                        preventOverlap: true,
                        nodeStrength: -170,  //节点的引力，负数代表斥力
                        // center: [ 500, 200 ],     // 可选，默认为图的中心
                        center: [width / 2, height / 2],
                    },
                    defaultNode: {
                        size: nodeSize,
                        type: 'circle',
                        style: {
                            lineWidth: 2,
                            fill:"2B384E",
                            stroke:"2B384E"
                        },
                        labelCfg: {
                            position: 'bottom',
                            position: 'bottom',
                            style: {
                                fill: '#fff',
                                stroke: '#191b1c',
                            },
                        },
                        icon: {
                            show: true,
                            width: nodeIconSize,
                            height: nodeIconSize
                            // img: 'https://gw.alipayobjects.com/zos/basement_prod/012bcf4f-423b-4922-8c24-32a89f8c41ce.svg',
                            /* icon's size, 20 * 20 by default: */
                            //   width: 40,
                            //   height: 40
                        },
                    },
                    defaultEdge: {
                        style:{  //TODO:可以修改箭头的样式  https://g6.antv.antgroup.com/manual/middle/elements/edges/arrow
                            endArrow:true,
                            realEdgeOpacity,
                            strokeOpacity: realEdgeOpacity,
                            lineWidth:2,
                        },
                        
                    },
                    nodeStateStyles: {
                        activeByLegend: {
                            lineWidth: 10,
                            strokeOpacity: 0.5
                        },
                        inactiveByLegend: {
                            
                        },
                        active: {
                            lineWidth: 10,
                            strokeOpacity: 0.5
                        },
                        inactive:{ //必须设置这个，否则node样式会变化
                            fill:"#2B384E",
                            stroke:"#2B384E"
                        }
                    },
                    edgeStateStyles: {
                        activeByLegend: {
                            lineWidth: 3
                        },
                        inactiveByLegend: {
                            opacity: 0.5
                        }
                    },
                    animate: true,
                    // 设置为true，启用 redo & undo 栈功能
                    enabledStack: true,
                    plugins: [contextMenu,tooltip],
                });
                this.graphCanvas = graph;
  
              
                graph.data({
                    nodes: data.nodes,
                    edges: data.edges.map(function (edge, i) {
                        edge.id = 'edge' + edge.id;
                        return Object.assign({}, edge);
                    }),
                });
                graph.render();
                graph.on('node:dragstart', function (e) {
                    graph.layout();
                        refreshDragedNodePosition(e);
                });
                graph.on('node:drag', function (e) {
                    const forceLayout = graph.get('layoutController').layoutMethods[0];
                    forceLayout.execute();
                    refreshDragedNodePosition(e);
                });
                graph.on('node:dragend', function (e) {
                    e.item.get('model').fx = null;
                    e.item.get('model').fy = null;
                });
                graph.on('afteradditem',function (e) {
                    console.log("after add回调函数")
                    graph.layout();
                    refreshDragedNodePosition(e);
                });

                // graph.on('node:mouseenter', (evt) => {
                // const { item } = evt;
                // graph.setItemState(item, 'active', true);
                // });

                // graph.on('node:mouseleave', (evt) => {
                // const { item } = evt;
                // graph.setItemState(item, 'active', false);
                // });
                if (typeof window !== 'undefined')
                window.onresize = () => {
                    if (!graph || graph.get('destroyed')) return;
                    if (!container || !container.scrollWidth || !container.scrollHeight) return;
                    graph.changeSize(container.scrollWidth, container.scrollHeight);
                };
            });

            function refreshDragedNodePosition(e) {
            const model = e.item.get('model');
            model.fx = e.x;
            model.fy = e.y;
            }
        },
        noMoreInfo() {
            this.$notify({
            title: '检索成功',
            message: '该节点暂无更多关联信息',
            type: 'success'
            });
        },
        haveMoreInfo(nodeCount,edgeCount){
            this.$notify({
            title: '检索成功',
            message: '共查到新的节点'+nodeCount+"个,新的关系"+edgeCount+"个",
            type: 'success'
            });
        }
    },
    mounted(){
        
    }
}
</script>
<style scoped>
/deep/ .el-descriptions-item__label.is-bordered-label {
  font-weight: bold;
  color: #909399;
  background: #fafafa;
  width: 120px;
}

/deep/.el-descriptions-item__content {
  word-break: break-word;
  overflow-wrap: break-word;
  width: 300px;
  height:30px
}

.null-text{
color:#a1a0a1;
}

/deep/.el-descriptions--medium.is-bordered .el-descriptions-item__cell {
  background-color: #3c3a3a;
  color: white;
}
</style>

<style scoped>
.info-box {
    float: left;
    box-shadow: 0 0 1px rgba(0,0,0,.125),0 1px 3px rgba(0,0,0,.2);
    border-radius: .25rem;
    display: -ms-flexbox;
    display: flex;
    margin-bottom: 1rem;
    min-height: 80px;
    padding: .5rem;
    position: relative;
    width: 180px;
}
.info-box .info-box-icon {
    /* border-radius: .25rem; */
    -ms-flex-align: center;
    align-items: center;
    display: -ms-flexbox;
    display: flex;
    font-size: 1.875rem;
    -ms-flex-pack: center;
    justify-content: center;
    text-align: center;
    width: 50px;
}

.info-box .info-box-content {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-direction: column;
    flex-direction: column;
    -ms-flex-pack: center;
    justify-content: center;
    line-height: 1.8;
    -ms-flex: 1;
    flex: 1;
    padding: 0 10px;
    overflow: hidden;
}

.info-box .info-box-text, .info-box .progress-description {
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.info-box .info-box-number {
    display: block;
    margin-top: .25rem;
    font-weight: 700;
}
</style>

<style scoped>
/deep/.el-descriptions {
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    font-size: 14px;
    color: #9ea0a2;
}
/deep/.el-descriptions__body {
    color: #9ea6b5;
    background-color: #343A40;
}
</style>
