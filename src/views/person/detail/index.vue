<template>
    <div class="page" style="padding:20px;height:700px;">
        <el-row>
            <el-card>
                 <div style="font-size: 20px;margin-bottom: 7px;">人员画像</div>
                 <!-- <span>人员画像，介绍xxxxx</span> -->
            </el-card>
        </el-row>

        <el-row :gutter="20" style="margin-top:20px;">
            <el-col :span="6" :xs="24">
              <person-card :personInfo="personInfo" />
            </el-col>
    
            <el-col :span="18" :xs="24">
              <el-card body-style="min-height:526px;">
                <el-tabs v-model="activeTab">
                  <el-tab-pane label="旗下公司" name="company">
                    <!-- 表格1：公司 -->
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
                          <!-- <i class="el-icon-user"></i> -->
                          法定代表人
                        </template>
                        <div class="null-text" v-if="personInfo.personName==null">暂无</div>
                        <el-tag v-else size="small" type="plain" style="border-color:purple;color: purple;">{{personInfo.personName}}</el-tag>
                      </el-descriptions-item>
                    
                      <el-descriptions-item>
                        <template slot="label">
                          <!-- <i class="el-icon-location-outline"></i> -->
                          注册资本
                        </template>
                        <div class="null-text" v-if="personInfo.companyList[0].registerCapital==null">暂无</div>
                        <div v-else>{{personInfo.companyList[0].registerCapital}}</div>
                      </el-descriptions-item>
              
                      <el-descriptions-item>
                        <template slot="label">
                          <!-- <i class="el-icon-tickets"></i> -->
                          注册时间
                        </template>
                        <div class="null-text" v-if="personInfo.companyList[0].registerTime==null">暂无</div>
                        <el-tag v-else size="small" type="plain" style="border-color:purple;color: purple;">{{personInfo.companyList[0].registerTime}}</el-tag>
                      </el-descriptions-item>
              
                      <el-descriptions-item>
                        <template slot="label">
                          <!-- <i class="el-icon-office-building"></i> -->
                          公司状态
                        </template>
                        <div class="null-text" v-if="personInfo.companyList[0].companyStatus==null">暂无</div>
                        <div v-else>{{personInfo.companyList[0].companyStatus}}</div>
                      </el-descriptions-item>
                      <el-descriptions-item>
                          <template slot="label">
                            <!-- <i class="el-icon-office-building"></i> -->
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
                    
                    <!-- 表格2：网站 -->
                    
                  </el-tab-pane>
                  <el-tab-pane label="旗下网站" name="website">
                    
                  </el-tab-pane>
                  <el-tab-pane label="Timeline" name="timeline">
                    <timeline />
                  </el-tab-pane>
                  <el-tab-pane label="关系链" name="group">
                    展示合作图谱？展示所在团伙情况，以及id，给予跳转到团伙详情的链接
                    <div id="person-container"></div>
                  </el-tab-pane>
                </el-tabs>
              </el-card>
            </el-col>
    
          </el-row>

       

        <!-- <el-row>
            <el-card>
                人员信息（信用良好/）
            </el-card>
            <el-card>
                旗下公司
                <a-collapse v-model="activeKey">
                    <a-collapse-panel key="1" header="This is panel header 1">
                      <p>{{ text }}</p>
                    </a-collapse-panel>
                    <a-collapse-panel key="2" header="This is panel header 2" :disabled="false">
                      <p>{{ text }}</p>
                    </a-collapse-panel>
                    <a-collapse-panel key="3" header="This is panel header 3" disabled>
                      <p>{{ text }}</p>
                    </a-collapse-panel>
                  </a-collapse>
            </el-card>
            <el-card>
                旗下网站:列表/善意/恶意占比，若恶意>善意：此人员旗下恶意下载网站多于正常网站，可能涉及xxxxx；此人员旗下网站均正常，信用良好；均恶意；

            </el-card>

        </el-row>

        <el-row>
            <el-card>
                涉及团伙/合作链条
            </el-card>
            
        </el-row> -->
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
            activeTab: 'company',
            personInfo:'',
            pid:'',
            graph:'',
            graphCanvas:'',
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
            this.showGraph()
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
            })
        },
        showGraph(depth=2){ //传入深度，默认为2度关系
            const containerId = "person-container"
            const container = document.getElementById(containerId);
            const width = container.scrollWidth ||300;
            const height = container.scrollHeight || 420; //TODO:原本为450，这里修改画布的高度
            const canvasBackgroundColor = '#363B40';
            const darkBackColor = '#2B384E'; //TODO:这里修改节点的背景颜色 原本rgb(43, 47, 51)
            container.style.backgroundColor = canvasBackgroundColor; //TODO:背景颜色?
            const nodeSize = 25;
            const nodeIconSize = 25;
            const realEdgeOpacity = 0.4;
            insertCss(`
            .g6-component-tooltip {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 0px 10px 24px 10px;
                box-shadow: rgb(174, 174, 174) 0px 0px 10px;
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

                const subjectColors = [
                    '#5F95FF', // blue
                    '#61DDAA',
                    // '#65789B',
                    '#F6BD16',
                    '#9661BC', //purple
                    '#78D3F8',
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
                const clusterNode = ["Website","Company","Person","Ip","Redirect"];
                const clusterEdge = ["BELONGS_TO","DOWNLOAD_FROM","HAS_IP","HAS_COMPANY","SIMILAR_TO"];
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
                    node.style.fill = "#2B384E";   //colorSets[cid].mainStroke; 
                    node.style.stroke = "#2B384E";//colorSets[cid].mainStroke; 
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
                        // <ul>
                        //     <li>节点类型:${e.item.getType()}</li>
                        // </ul>
                        if(e.item.getType()=="node"){
                            outDiv.innerHTML = `
                            <h4>节点信息</h4>
                            <ul>
                                <li>节点类型:<button style="font-weight: bold;"> ${e.item.getModel().label}</button></li>
                            </ul>
                            <ul>
                                <li>节点名称: ${e.item.getModel().properties["name"] || e.item.getModel().id}</li>
                            </ul>
                            <ul>
                                <li>PageRank: ${result[e.item.getModel().id]}</li>
                            </ul>
                        `;
                        }
                        else if(e.item.getType()=="edge"){
                            outDiv.innerHTML = `
                                <h4>边信息</h4>
                                <ul>
                                    
                                    <li>边类型:<button style="font-weight: bold;"> ${e.item.getModel().label}</button></li>
                                </ul>
                            `;
                        }
                        return outDiv;
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
                        if (evt.target && evt.target.isCanvas && evt.target.isCanvas()) { //右键画布
                            return `<ul>
                            <li id='show'>显示全部隐藏节点</li>
                            <li id='collapseAll'>Collapse all Clusters</li>
                            </ul>`;
                        } 
                        else if (!item) return;
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
                        center: [ 500, 200 ],     // 可选，默认为图的中心
                        // center: [width / 2, height / 2],
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
                    plugins: [legend,tooltip,contextMenu],
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
    },
    mounted(){
        this.getPersonInfo()
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