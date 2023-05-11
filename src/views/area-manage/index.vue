<template>
    <div>
      <el-row>
        <el-card>
             <div style="font-size: 20px;margin-bottom: 7px;">全国地区态势</div>
             <span>追踪团伙构成恶意下载网站、背后公司组成、涉及人员</span>
             当前团伙：{{ cid }}
             <el-divider></el-divider>
        </el-card>
    </el-row>
        <!-- 
          TODO:地区治理：
        1、一个省份下的相关网站/恶意网站；IP；
        2、他们所属的公司
        3、人员
        4、一个地区下的增长情况
        
        5、监管人员可以mark可疑的网站/公司/人员
        6、监管人员可以设置自己的管理地区

        下载分析报告 -->

        <el-card>
          <ChinaMap style="height:600px"/>
        </el-card>
        
        <el-card>
          <ChinaPie/>
        </el-card>
        
    </div>
</template>

<script>
import echarts from 'echarts'
import ChinaMap from './ChinaMap.vue';
import ChinaPie from './ChinaPie.vue';

export default {
  components:{
    ChinaMap,
    ChinaPie,
  },
  mounted() {
   
  }
}
</script>