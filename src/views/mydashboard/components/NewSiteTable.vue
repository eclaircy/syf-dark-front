<template>

  <el-table :data="tableData" border style="width: 100%" >
  <!--     :header-cell-style="{background:'#f1f1f1',color:'#606266',borderColor:'#C0C0C0'}"
    :cell-style="{borderColor:'#C0C0C0'}" -->
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
          <a-tag  color="rgb(166 13 13)">恶意网站</a-tag>
        </template>
    </el-table-column>
  </el-table>

</template>
  
<script>
export default {
  data() {
    return {
      tableData:'',
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

</style>