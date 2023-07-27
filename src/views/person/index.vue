<template>
    <div style="padding:20px;">
        <el-row>
            <el-card>
                 <div style="font-size: 20px;margin-bottom: 7px;">人员追踪</div>
                 <span>根据公司、网站、姓名追踪人员，并查看人员画像</span>
                 <!-- <el-divider></el-divider> -->
            </el-card>
        </el-row>

        <div class="search-container"> 
          <el-input placeholder="请输入线索"  clearable style="width:240px;margin-right:30px;margin-left:20px;" v-model="search.input1">
            <template slot="prepend">人员</template>
          </el-input>

          <el-input placeholder="请输入线索"  clearable style="width:240px;margin-right:30px;margin-left:20px;" v-model="search.input2">
              <template slot="prepend">公司</template>
          </el-input>

          <el-input placeholder="请输入线索"  clearable style="width:240px;margin-right:30px;margin-left:20px;" v-model="search.input3">
              <template slot="prepend">网站</template>
          </el-input>
          
          <el-button size="medium" type="primary" @click="searchPerson()">查询<i class="el-icon-search"></i></el-button>
          <el-button size="medium" type="primary" @click="handleClear()">清空线索</el-button>
        </div>

        <el-row>
          <el-col :span="19"> 
            <person-simple-card :personInfoByPage="personInfoByPage.records"></person-simple-card>
                  <!-- <SiteSimpleCard :sitesInfoByPage="sitesInfoByPage.records"/> -->
          </el-col>
      </el-row>

      <div class="pagination-container"> 
        <div class="pagination">
          <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page.sync="paginations.currentPage"
            :page-size="paginations.pageSize"
            :layout="paginations.layout"
            :total="paginations.totalPage">
          </el-pagination>
        </div>
      </div>

        <!-- <el-row>
            搜索：根据人员/公司，最后查到的是人
            
            员
            最新增加的人员/公司；增长情况

        </el-row> -->

        <!-- <el-row :gutter="5">
            <el-col :span="12">
                <el-card>
                    新增可疑人员/公司
                    <a-list item-layout="horizontal" :data-source="data_a">
                      <a-list-item slot="renderItem" slot-scope="item, index">
                        <a-list-item-meta
                          description="Ant Design, a design language for background applications, is refined by Ant UED Team"
                        >
                          <a slot="title">aaaaaaa</a>
                          <a-avatar
                            slot="avatar"
                            src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                          />
                        </a-list-item-meta>
                      </a-list-item>
                    </a-list>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card></el-card>
            </el-col>    
        </el-row> -->
    </div>
</template>

<script>

import PersonSimpleCard from "./component/PersonSimpleCard.vue"

export default {
    data(){
        return{
          personInfoByPage:[],
          emptySerchCondition:false,
          search:{
            input1:'', // 人员
            input2:'', // 公司
            input3:'', // 网站
          },
          paginations:{
              currentPage: 1,
              totalPage: '',
              pageSize: 8,
              layout:"total, prev, pager, next, jumper",
          }
        }
    },
    components:{
      PersonSimpleCard,
    },
    methods:{
        getPerson(){
          // var page = 1;
          // var searchParam = ''
          //   for (let key in this.search) {
          //       console.log(`key: ${key}, value: ${this.search[key]}`);
          //       if(key=="input1" && this.search[key]!=''){
          //           searchParam = searchParam + this.select.select1 +"="+ this.search[key]
          //       }
          //       else if(key=="input2" & this.search[key]!=''){
          //           searchParam = searchParam + '&' + "company" +"="+  this.search[key]
          //       }
          //       else if(key=="input3" & this.search[key]!=''){
          //           searchParam = searchParam + '&' + "person" +"="+  this.search[key]
          //       }
          //       else if(key=="input4" && this.search[key]!=''){
          //           searchParam = searchParam +"&" + this.select.select2 +"="+  this.search[key]
          //       }
          //   }
          // console.log(searchParam)
          this.axios({
            method:"get",
            url:"api/person/all?limit=8&"+"page="+this.paginations.currentPage
          }).then(res=>{
            this.personInfoByPage=res.data;
            this.paginations.totalPage=res.data.total;
          })
        },
        //分页
        handleSizeChange(val) {
            console.log(`每页 ${val} 条`);
        },
        handleCurrentChange(val) { //当前页val
            this.paginations.currentPage=val;
            // this.getPerson();
            if(this.emptySerchCondition==true){
              this.getPerson();
            }else{

            }
            
            // console.log(`当前页: ${val}`);
        },
        handleClear(){
          for (let key in this.search) {
            this.search[key]="";
          }
          this.emptySerchCondition=true;
        },
        searchPerson(){
          // "/person/search?size=8&page=1&url=&personName=许&companyName="
          if(this.emptySerchCondition==true){
            this.getPerson()
          }else{
            this.paginations.currentPage=1;
            this.axios({
              method:"get",
              url:"api/person/search?size=8&"+"page=1&"+"url="+this.search.input3+"&personName="+this.search.input1+"&companyName="+this.search.input2
            }).then(res=>{
              this.personInfoByPage=res.data;
              this.paginations.totalPage=res.data.total;
            })          
          }
        }
    },
    mounted(){
      this.getPerson();
    }
}
</script>

<style scoped>
.ant-list-split .ant-list-item {
    border-bottom: 1px solid #656565;
}
.ant-list-item-meta-title >a{
    margin-bottom: 4px;
    color: rgb(226 226 226 / 74%);
    font-size: 14px;
    line-height: 22px;
}
.ant-list-item-meta-description {
    color: rgb(226 226 226 / 74%);
    font-size: 14px;
    line-height: 22px;
}
.search-container{
  background: #343A40;
  padding: 10px;
  margin-bottom: 20px;
  height: 62px;
 
  border-radius:0px;
  overflow:hidden; 
}

.pagination-container{
  background-color: #343A40;
  height: 52px;
 
  border-radius:0px;
  margin-top:10px;
}
.pagination{
  margin-top:10px;
  margin-bottom: 10px;
  margin-left: 319.8px;
}
/deep/.el-button{
  background-color:#9487dd;border-color:#9487dd
}
/deep/.el-button:hover{
  background-color:#7265ba;border-color:#8f82d7
}
</style>