<template>

  <el-table :data="tableData" border style="width: 100%">
      <el-table-column
          prop="domain"
          label="域名"
          width="180">
      </el-table-column>
      <el-table-column
          prop="title"
          label="网站标题">
      </el-table-column>

      <el-table-column prop="type" label="类型">
          <template slot-scope="{row}">
              <el-tag :type="row.status | statusFilter">
                  {{ row.status }}
              </el-tag>
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
          }, {
            domain: '2016-05-03',
            title: '王小虎',
            type: '良性'
          }, {
            domain: '2016-05-03',
            title: '王小虎',
            type: '良性'
          }
        ]
        }
      }
    }
  </script>