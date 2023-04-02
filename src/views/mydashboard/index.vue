<template>
  <div class="dashboard-editor-container">
    <!-- <el-row>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>卡片名称</span>
          <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
        </div>
        <div v-for="o in 4" :key="o" class="text item">
          {{ '列表内容 ' + o }}
        </div>
      </el-card>  
    </el-row> -->
    <h4>TODO:
      1、展示数值：（全部/恶意）网站数、ip数；   各种组件的使用数量
      2、统计
      每年的新出现数量、累计总数量  
      使用年份

    </h4>

    <panel-group />
    
    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <BarChart/>
    </el-row>
    
    <el-row gutter=32>
      <el-col  :span="12">
        <div class="chart-wrapper">
          <CreatedYearWithArea />
        </div>
      </el-col>
      <el-col  :span="12">
        <!-- 中国地图+散点：展示恶意网站/ip分布 -->
        <ChinaMap1 /> 
      </el-col>
    </el-row>
    <el-row gutter=32>
      <el-col  :span="8">
        <!-- echarts的关系图，先去掉 -->
        <!-- <MalwareSitesGraphOverview />   -->
      </el-col>
      <el-col  :span="8">
        <transaction-table />
      </el-col>
      <el-col  :span="8">
        <el-card>
          <RoseChart/>
        </el-card>
      </el-col>    
        <!-- <Zhu/> -->
    </el-row>

    <el-row>
      <el-col :span="12">
        <StackArea/>
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
    RoseChart
  }
}

</script>

<style scoped>
.chart-wrapper {
  background: #fff;
  padding: 16px 16px 0;
  margin-bottom: 32px;
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}

.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;
}

</style>
