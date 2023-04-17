<template>
  <div class="dashboard-editor-container">

    <!-- <h4>TODO:
      1、展示数值：（全部/恶意）网站数、ip数；公司？； 
      2、统计
      每年的新出现数量、累计总数量  
      使用年份
      TODO:https://g2plot.antv.antgroup.com/zh/examples/dynamic-plots/animation/#animation-column 柱状图动画、颜色
    </h4> -->

    <!-- <panel-group /> -->
    <el-row style="margin-top:25px;">
      <PanelGroup />
    </el-row>
    
    <el-row :gutter=20 style="">
      <el-col :span="16">
        <el-card class="el-card" style="height:410px" >
          <div class="card-title">整体变化趋势图</div>
          <PanelStack/>
          <!-- <PanelLine/> -->
        </el-card>
        
      </el-col>
      <el-col :span="8">
        <el-card class="el-card" style="height:410px">
          <div class="card-title" style="margin-bottom:5px">占据比例</div>
          <PieChart/>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter=10>
      <el-col  :span="11">
        <!-- <el-card style="margin-bottom:5px;height:200px">
          <div class="card-title" >网站-地区分布柱状图
            <AreaRose/>
          </div>
        </el-card> -->
        <el-card style="height:420px"> 
            <div class="card-title">网站-地区分布柱状图
            <AreaBar/>
        </div>
        </el-card>
      </el-col>
      <!-- 15:9 -->
      <el-col  :span="13">
        <!-- 中国地图+散点：展示恶意网站/ip分布 -->
        <el-card style="height:420px;overflow:hidden">
          <WorldDrillMap/>
             <!-- <ChinaMap1 /> -->
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter=20>
      <el-col  :span="16">
        <el-card style="height:450px">
          <div class="card-title">网站建立时间变化图</div>
          <SiteYearGraph/>
        </el-card>
        

      </el-col>
      <el-col  :span="8">
        <el-card style="height:450px">
          <el-carousel height="430px">
            <el-carousel-item>
            <div class="card-title">最新检测网站</div>  
            <NewSiteTable/>
            </el-carousel-item>
            <!-- <el-carousel-item>
              <div class="card-title">最新相关人员/公司</div>
              <NewPersonTable/>  
            </el-carousel-item> -->
          </el-carousel>
        </el-card>
      </el-col>    
    </el-row>


    
  </div>
</template>

<script>
import PanelStack from './components/PanelStack'
import NewSiteTable  from './components/NewSiteTable'
import SiteYearGraph from "./components/SiteYearGraph"
import PanelGroup from './components/PanelGroup.vue'
import AreaBar from './components/AreaBar.vue'
import PieChart from './components/PieChart.vue'
import AreaRose from './components/AreaRose.vue'
import WorldDrillMap from './components/WorldDrillMap.vue'
import NewPersonTable from "./components/NewPersonTable.vue"
import PanelLine from "./components/PanelLine.vue"

export default {
  name: 'MyDash',
  components: {
    PanelGroup, 

    PanelStack,
    PanelLine,
    PieChart,

    WorldDrillMap,
    AreaBar,
    AreaRose,

    SiteYearGraph,
    NewSiteTable,
    NewPersonTable
  },
  data() {
    return {
      

    }
  },
  methods: {
    // getPanelGroup(){
    //   //获取总统计数量
    //   this.axios({
    //       url:"api/sites/statistic",
    //       method:'get'
    //   }).then(res=>{
    //       console.log(res);
    //       this.countGroup=res.data;
    //   })
    // },
    getPanelStack(){

    },
    getPieChart(){

    },
    getWorldDrillMap(){

    },
    getArea(){

    },
    getSiteYearGraph(){

    }

  },
  mounted(){
    
  }
}

</script>

<style  lang="scss" scoped>

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}

.dashboard-editor-container {
  padding: 24px;
  background-color: #F8F9FE; 
  position: relative;
}

.el-row{ //每行之间的间距
  margin-bottom:25px;
}

//TODO:统一设置el-card圆角样式
.el-card{
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 5px rgba(0, 0, 0, .04)
}
.card-title{
  font-weight: bold;
  font-size: 16px;
  color: #303133;
  margin-bottom: 20px;
}
</style>
<!-- #F8F9FE -->
<!-- 

  .dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245); 
  position: relative;
}

 -->