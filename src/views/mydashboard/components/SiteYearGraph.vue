<template>

    <div id="site-year-container">
    </div>


</template>

<style scoped>
  .container1{
    scrollWidth: 683.3px;
    scrollHeight: 400px;
  }
</style>

<script>
import G6 from '@antv/g6';
export default {
    data(){
        return{

        }
    },
    methods:{
        show(){
          const container = document.getElementById('site-year-container');
          const width = container.scrollWidth;  //节点画布的宽度
          const height = (container.scrollHeight || 430) - 150;  //节点画布的高度
          const nodeSize = 20;
          const timeBarHeight = 140;  //时间轴高度
          const timeBarData = [];
          const canvasBackgroundColor = '#363b40';
          container.style.backgroundColor = canvasBackgroundColor;
          const darkBackColor = 'rgb(43, 47, 51)'; //TODO:这里修改节点的背景颜色 原本rgb(43, 47, 51)
          const disableColor = '#777';
          const theme = 'dark'; //原本为dark  可选：dark、default
          const subjectColors = [
            '#5F95FF', // blue
            '#61DDAA',
            '#65789B',
            '#F6BD16',
            '#7262FD',
            '#78D3F8',
            '#9661BC',
            '#F6903D',
            '#008685',
            '#F08BB4',
          ];
          const colorSets = G6.Util.getColorSetsBySubjectColors(
              subjectColors,
              darkBackColor,
              theme,
              disableColor,
          );

          const data = {
            nodes: [],
            edges: [],
          };
          for (let i = 0; i < 100; i++) {
            const id = `node-${i}`;
            data.nodes.push({
              id,
              date: `2020${i}`,
              //value: Math.round(Math.random() * 300),
            });

            data.edges.push({
              source: `node-${Math.round(Math.random() * 90)}`,
              target: `node-${Math.round(Math.random() * 90)}`,
            });
          }
          //格式为{
          //    id:1, date:"yyyymm"
          //  }
          console.log(data.nodes)
          console.log(data.edges)
          
          for (let i = 0; i < 100; i++) {
            timeBarData.push({
              date: `2020${i}`,
              value: Math.round(Math.random() * 300),
            });
          }
          console.log("time bar data:")
          console.log(timeBarData)

          const timebar = new G6.TimeBar({
            x: 0,
            y: 0, //原本是0，他们的含义是什么？
            width,
            height: timeBarHeight,
            padding: 0, //原本是10
            type: 'trend',
            trend: {
              data: timeBarData,
            },
          });

          // constrained the layout inside the area
          const constrainBox = { x: 80, y: 0, width: 680, height: 340 };

          const onTick = () => {
            let minx = 99999999;
            let maxx = -99999999;
            let miny = 99999999;
            let maxy = -99999999;
            let maxsize = -9999999;
            data.nodes.forEach((node) => {
              if (minx > node.x) {
                minx = node.x;
              }
              if (maxx < node.x) {
                maxx = node.x;
              }
              if (miny > node.y) {
                miny = node.y;
              }
              if (maxy < node.y) {
                maxy = node.y;
              }
            });
            const scalex = (constrainBox.width - nodeSize / 2) / (maxx - minx);
            const scaley = (constrainBox.height - nodeSize / 2) / (maxy - miny);
            data.nodes.forEach((node) => {
              node.x = (node.x - minx) * scalex + constrainBox.x;
              node.y = (node.y - miny) * scaley + constrainBox.y;
            });
          };
          const realEdgeOpacity= 0.2;
          const graph = new G6.Graph({
            container: 'site-year-container',
            width,
            height,
            linkCenter: true,
            plugins: [timebar],
            layout: {
              type: 'force',
              preventOverlap: true,
              onTick,
            },
            defaultNode: {
              size: nodeSize,
              style: {
                fill: colorSets[0].mainFill || colorSets[0].mainFill || '#2B384E',
                opacity: 0.9,
              },
              
            },
            defaultEdge:{
              style: {
                stroke: '#acaeaf',
                realEdgeStroke: '#acaeaf', //'#f00',
                realEdgeOpacity,
                strokeOpacity: realEdgeOpacity,
              },
            },
            modes: {
              default: ['drag-node','drag-canvas', 'zoom-canvas'],  //zoom用于缩放画布
            },
          });
          graph.data(data);
          graph.render();

          if (typeof window !== 'undefined')
            window.onresize = () => {
              if (!graph || graph.get('destroyed')) return;
              if (!container || !container.scrollWidth || !container.scrollHeight) return;
              graph.changeSize(container.scrollWidth, container.scrollHeight - 100);
            };

        }
    },
    mounted(){
        this.show()
    }
}
</script>

