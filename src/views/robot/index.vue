<template>
    <div style="padding:20px;">
        <el-row :gutter="20">
            <el-col :span="12">
                <div style="border-radius:14px;height:625px;border: 1px solid #fff;padding:15px;">
                    <el-scrollbar style="height:500px;" wrap-style="overflow-x:hidden;" id="chatroom" ref="chatroom" >
                        <div ref="innerRef">
                    
                        <div v-for="(item,index) in chat">
                            <div v-if="item.side=='left'" class="chat-content-leftside" :key="index">
                                <div class="d-flex">
                                    <img src="./robot.png" width="48" height="48" class="rounded-circle" alt="">  
                                    <div class="flex-grow-1 ms-2">
                                        <p class="mb-0 chat-time">ChatRoboT</p>
                                        <p class="chat-left-msg">{{item.content}}</p>
                                    </div>
                                </div>
                            </div>
                            
                            <div v-else class="chat-content-rightside"  :key="index">
                                <div class="d-flex">
                                    <div class="flex-grow-1 me-2">
                                        <p class="mb-0 chat-time text-end">You</p>
                                        <p class="chat-right-msg">{{item.content}}</p>
                                    </div>
                                </div>
                            </div>
                        
                        </div>
                    </div>
                    </el-scrollbar>
                     <el-divider></el-divider>
                    <div style="display:flex;margin-top:10px;">
                        <el-input v-model="input" size="medium" style="display: inline-block;margin-left:20px;"></el-input>
                        <el-button style="display: inline-block;" @click="send()">发送</el-button>
                        <el-button style="display: inline-block;" @click="clear()">清空</el-button>
                        <!-- <el-button style="display: inline-block;" @click="add('left','测试水水水水水水水水水水水水水水水水')">发送2</el-button> -->
                    </div>
                    
                </div>
            </el-col>

            <el-col :span="12">
                <div style="border-radius:14px;height:625px;border: 1px solid #fff;padding:1px;">
                    <!-- <el-empty description="描述文字"></el-empty> -->
                    <div id="graph-container" style="height:100%;width:100%;border-radius:14px;"></div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Qs from 'qs'
import axios from 'axios'
import G6 from '@antv/g6';
import insertCss from 'insert-css';
export default {
    data() {
        return {
            input:'',
            answer:'',
            chat:[{side:"left",content:"您好，这里是ChatRobot，有什么问题需要帮助吗？😊"},],
            graph:'',
            graphCanvas:'',
            fistGraphShow:true,
        }
    },
    methods: {
        send(){
            const input = this.input;
            this.input = '';
            this.add("right",input);
            // this.scrollToBottom();
            this.add("left","ChatRobot正在为您检索中,请稍后。😊");
            // this.scrollToBottom();
            //我想查询http://www.pc9.com网站的关系图谱
            // const data = {input:'我想查询http://tool.52jscn.com网站的关系图谱'} 
            const data = {input:input}
            axios.post("http://127.0.0.1:5000/a", data,{headers: {
                'Content-Type': 'application/json'
            }})
            .then(res=>{
                console.log('res=>',res.data);
                this.graph=res.data.graph;
                this.add("left",res.data.answer+"😊"); 
                // this.scrollToBottom();
                //只有当nodes数量大于0时才显示图谱
                if(res.data.graph.nodes!==undefined&&res.data.graph.nodes.length>0){
                    if(this.fistGraphShow==true){
                        this.showGraph(this.graph);
                        this.fistGraphShow=false;
                    }else{
                        this.changeGraphData(this.graph);   
                    }
                } 
            })
            // this.scrollToBottom();
        },
        add(side,content){
            this.chat.push({side:side,content:content})
            this.scrollToBottom();
        },
        clear(){
            this.chat = [{side:"left",content:"您好，这里是ChatRobot，有什么问题需要帮助吗？😊"},]
        },
        changeGraphData(newData) {
            // 更新数据并重新渲染画布
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
            const backColor = '#2B384E';//
            const theme = 'dark';
            const disableColor = '#777';
            const colorSets = G6.Util.getColorSetsBySubjectColors(
                subjectColors,
                backColor,
                theme,
                disableColor,
            );
            //给新节点上色
            const clusterNode = ["Website","Company","Person","Ip","Redirect"];
            const clusterEdge = ["BELONGS_TO","DOWNLOAD_FROM","HAS_IP","HAS_COMPANY","SIMILAR_TO"];
            newData.nodes.forEach(function (node) {
                const cid = clusterNode.indexOf(node.label[0]);
                node.legendType=node.label[0];
                if (!node.style) {
                    node.style = {};
                }
                node.icon = {
                    show:true,
                    img:require("@/assets/nodes/"+node.label[0]+".png"),
                };
                node.style.fill = "#2B384E"; //subjectColors
                node.style.stroke = "#2B384E"; //strokes[cid % strokes.length];
            });
            newData.edges.forEach(edge => {
                const cid = clusterEdge.indexOf(edge.label);
                edge.legendType=edge.label;
                edge.id="edge"+edge.id;
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
            // 更新数据并重新渲染画布
            this.graphCanvas.changeData(newData);
        },
        showGraph(data){
            const containerId = "graph-container"
            const container = document.getElementById(containerId);
            const width = 580;
            const height = 580; //TODO:原本为450，这里修改画布的高度
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

            //3、分类
            const clusterNode = ["Website","Company","Person","Ip","Redirect"];
            const clusterEdge = ["BELONGS_TO","DOWNLOAD_FROM","HAS_IP","HAS_COMPANY","SIMILAR_TO"];
            // const clusterNode = ["Domain","Company","Person","Ip","Cert"];
            data.nodes.forEach(function (node) {
                const cid = clusterNode.indexOf(node.label[0]);
                node.legendType=node.label[0];
                // node.id = str(node.id);
                if (!node.style) {
                    node.style = {};
                }
                node.icon = {
                    show:true,
                    img:require("@/assets/nodes/"+node.label[0]+".png"),
                };
                node.style.fill = "#2B384E";   //colorSets[cid].mainStroke; 
                node.style.stroke = "#2B384E";//colorSets[cid].mainStroke; 
            });
            
            // const clusterEdge = ["IS_SUB","FOUNDED_BY","HAS_IP","WORKS_FOR","HAS_CERT"];
            data.edges.forEach(edge => {
                const cid = clusterEdge.indexOf(edge.label);
                edge.legendType=edge.label;
                edge.id = 'edge' + edge.id;
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
                itemTypes: ['node', 'edge'],
                getContent: (e) => {
                    const outDiv = document.createElement('div');
                    outDiv.style.width = 'fit-content';
                    if(e.item.getType()=="node"){
                        outDiv.innerHTML = `
                        <h4>节点信息</h4>
                        <ul>
                            <li>节点类型:<button style="font-weight: bold;"> ${e.item.getModel().label[0]}</button></li>
                        </ul>
                        <ul>
                            <li>节点名称: ${e.item.getModel().properties["name"] || e.item.getModel().id}</li>
                        </ul>
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
                    // outDiv.innerHTML = `
                    // <h4>节点信息</h4>
                    // <ul>
                    //     <li>节点类型:<button style="font-weight: bold;"> ${e.item.getModel().label}</button></li>
                    // </ul>
                    // <ul>
                    //     <li>节点名称: ${e.item.getModel().properties["name"] || e.item.getModel().id}</li>
                    // </ul>
                    // <ul>
                    //     <li>PageRank: ${result[e.item.getModel().id]}</li>
                    // </ul>
                    // `;
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
                    center: [ width / 2, height / 2],     // 可选，默认为图的中心
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
                edges: data.edges
                // .map(function (edge, i) {
                //     edge.id = 'edge' + edge.id;
                //     return Object.assign({}, edge);
                // }),
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
 
            function refreshDragedNodePosition(e) {
            const model = e.item.get('model');
            model.fx = e.x;
            model.fy = e.y;
            }
        },
        scrollToBottom() {
            // this.$refs['chatroom'].wrap.scrollTop = 100000000
            this.$refs['chatroom'].wrap.scrollTop = this.$refs['chatroom'].wrap.scrollHeight
        },


    },
    mounted(){
        // this.send();
    },
    updated() {
        this.scrollToBottom();
        // console.log("new")
    }
}
</script>

<style scoped>
.chat-content-leftside .chat-left-msg {
    width: fit-content;
    background-color: #f6f2d7;
    padding: 0.80rem;
    border-radius: 12px;
    max-width: 480px;
    text-align: left;
    border-top-left-radius: 0;
}
.chat-content-rightside .chat-right-msg {
    width: fit-content;
    background-color: #dcedff;
    padding: 0.80rem;
    border-radius: 12px;
    float: right;
    max-width: 480px;
    text-align: left;
    border-bottom-right-radius: 0;
}
.flex-grow-1 {
    flex-grow: 1!important;
}

.rounded-circle {
    border-radius: 50%!important;
}
.d-flex {
    display: flex!important;
}
.text-end {
    text-align: right!important;
}
.ms-2 {
    margin-left: .5rem!important;
}

.chat-time {
    font-size: 13px;
    color: #c2c2c2;
}

/deep/.el-input__inner {
    background-color: #54575c;
    border-radius: 4px;
    border: 1px solid #b1b1b1;
    color: #eee;
    width: 400px;
    height:45px;
    
}

/deep/.el-button {
    background: #54575c;
    border: 1px solid #b1b1b1;
    border-color: #b1b1b1;
    color: #eee;
}
.el-button:hover{
    background: #434549;
}

/*
  进入和离开动画可以使用不同
  持续时间和速度曲线。
*/
.slide-fade-enter-active {
    transition: all 0.3s ease-out;
  }
  
  .slide-fade-leave-active {
    transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
  }
  
  .slide-fade-enter-from,
  .slide-fade-leave-to {
    transform: translateX(20px);
    opacity: 0;
  }
</style>