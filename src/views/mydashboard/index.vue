<template>
  <div class="dashboard-editor-container">

    <!-- <h4>TODO:
      1、展示数值：（全部/恶意）网站数、ip数；   各种组件的使用数量
      2、统计
      每年的新出现数量、累计总数量  
      使用年份
      TODO:https://g2plot.antv.antgroup.com/zh/examples/dynamic-plots/animation/#animation-column 柱状图动画、颜色
    </h4> -->

    <!-- <panel-group /> -->
    <el-row style="margin-top:25px;">
      <MyPanelGroup/>
    </el-row>
    
    <el-row gutter=20 style="">
      <el-col :span="16">
        <el-card class="el-card" style="height:410px" >
          <div class="card-title">整体变化趋势图</div>
          <StackArea/>
          <!-- <BarChart/> -->
        </el-card>
        
      </el-col>
      <el-col :span="8">
        <el-card class="el-card" style="height:410px">
          <div class="card-title" style="margin-bottom:5px">占据比例</div>
          <!-- <PercentBar/> -->
          <PieChart/>
        </el-card>
      </el-col>
    </el-row>

    <el-row gutter=10>
      <el-col  :span="9">
        <el-card style="margin-bottom:5px;height:210px">
          <div class="card-title" >网站-地区分布柱状图
            <!-- <RoseChart/> -->
            <MyRose/>
          </div>
        </el-card>
        <el-card style="height:210px"> 
            <div class="card-title">网站-地区分布柱状图
            <AreaBar/>
        </div>
        </el-card>
      </el-col>

      <el-col  :span="15">
        <!-- 中国地图+散点：展示恶意网站/ip分布 -->
        <el-card style="height:420px;overflow:hidden">
          <WorldDrillMap/>
             <!-- <ChinaMap1 /> -->
        </el-card>
      </el-col>
    </el-row>

    <el-row gutter=20>
      <el-col  :span="16">
        <el-card style="height:450px">
          <div class="card-title">网站建立时间变化图</div>
          <SiteWithYear/>
        </el-card>
        

      </el-col>
      <el-col  :span="8">
        <el-card style="height:450px">
          <div class="card-title">最新检测网站</div>
          <el-carousel height="430px">
            <el-carousel-item>
            <NewSiteTable/>
            </el-carousel-item>
            <el-carousel-item><NewPersonTable/></el-carousel-item>
          </el-carousel>

          <!-- TODO: -->
        </el-card>
      </el-col>    
    </el-row>


    
  </div>
</template>

<script>
import TransactionTable from '../dashboard/admin/components/TransactionTable'
import MalwareSitesGraphOverview from './components/MalwareSitesGraphOverview'
import PanelGroup from './components/PanelGroup'
import CreatedYearWithArea from './components/CreatedYearWithArea'
import ChinaMap1 from './components/ChinaMap1'
import Zhu from './components/Zhu'
import BarChart from './components/BarChart'
import StackArea from './components/StackArea'
import RoseChart from './components/RoseChart'
import AreaMultiChart from "./components/AreaMultiChart"
import NewSiteTable  from './components/NewSiteTable'
import SiteWithYear from "./components/SiteWithYear"
import Bullet from "./components/Bullet"
import MyPanelGroup from './components/candidate/MyPanelGroup.vue'
import PercentBar from './components/candidate/PercentBar.vue'
import AreaBar from './components/candidate/AreaBar.vue'
import PieChart from './components/candidate/PieChart.vue'
import MyRose from './components/candidate/MyRose.vue'
import WorldDrillMap from './components/candidate/WorldDrillMap.vue'
import NewPersonTable from "./components/candidate/NewPersonTable.vue"

export default {
  name: 'MyDash',
  components: {
    TransactionTable,
    MalwareSitesGraphOverview,
    PanelGroup,
    CreatedYearWithArea,
    ChinaMap1,
    Zhu,
    BarChart,
    StackArea,
    RoseChart,
    AreaMultiChart,
    NewSiteTable,
    SiteWithYear,
    Bullet,
    MyPanelGroup,
    PercentBar,
    AreaBar,
    PieChart,
    MyRose,
    WorldDrillMap,
    NewPersonTable
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