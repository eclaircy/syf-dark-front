<template>

  <el-table :data="tableData" border style="width: 100%" 
    :header-cell-style="{background:'#f1f1f1',color:'#606266',borderColor:'#C0C0C0'}"
    :cell-style="{borderColor:'#C0C0C0'}"
  >
    <el-table-column
        prop="domain"
        :show-overflow-tooltip="true"
        label="域名"
        >
    </el-table-column>

    <el-table-column
        prop="site_title"
        :show-overflow-tooltip="true"
        label="网站标题">
    </el-table-column>

    <el-table-column prop="is_malicious" label="类型">
        <template slot-scope="{row}">
          <el-tag v-if="row.id % 2==1" type="danger">恶意网站</el-tag>
          <el-tag v-else  type="success">正常网站</el-tag>
          <!-- <el-tag v-if="row.is_malicious===true" type="danger">恶意网站</el-tag>
          <el-tag v-else  type="success">正常网站</el-tag> -->
        </template>
    </el-table-column>
  </el-table>

</template>
  
<script>
export default {
  data() {
    return {
      tableData: [{
        domain: '2016-05-02',
        title: '王小虎',
        type: '恶意'
      }, {
        domain: '2016-05-04',
        title: '王小虎',
        type: '恶意'
      }, {
        domain: '2016-05-01',
        title: '王小虎',
        type: '良性'
      }, {
        domain: '2016-05-03',
        title: '王小虎',
        type: '良性'
      }
    ]
    }
  },
  methods: {
    getLatestSite(){
      this.axios({
        url:'api/sites/latest?limit=6',
        method:'get'
      }).then(res=>{
        this.tableData = res.data;
      })
    }
  },
  mounted(){
    this.getLatestSite()
  }
}
</script>

<style lang="css" scoped>
.el-table__header {
  background-color: #f1f1f1 !important;
}
</style>