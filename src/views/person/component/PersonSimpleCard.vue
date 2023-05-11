<template>
    <div class="site-cards-list">
        <el-card class="site-card" v-for="item in personInfoByPage" :key="item.id" shadow="hover">

            <div style="text-align: center!important;"> 
                <svg t="1683457700637" class="icon" viewBox="0 0 1095 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3284" width="30" height="30"><path d="M901.061633 693.651803a217.585111 217.585111 0 0 0 88.542846-175.100426 212.026367 212.026367 0 1 0-423.65568 0 215.996898 215.996898 0 0 0 88.939899 175.100426 357.347809 357.347809 0 0 0-194.953083 293.025204c0 20.249709 10.323381 36.131834 29.778984 36.131834h574.93292c19.455603 0 29.778984-15.882125 29.778984-36.131834a359.730128 359.730128 0 0 0-193.761923-293.025204z" fill="#9487dd" p-id="3285" data-spm-anchor-id="a313x.7781069.0.i0" class="selected"></path><path d="M556.022471 674.990306a299.775107 299.775107 0 0 1-63.131447-227.114385A284.290035 284.290035 0 0 1 603.668845 262.05506a287.46646 287.46646 0 0 1 261.658007-34.543621c77.425359 29.381931 79.410624 60.749128 88.542846 60.749127a35.337728 35.337728 0 0 0 34.940675-35.734781V192.173711A185.026755 185.026755 0 0 0 812.121734 0h-635.284994A185.026755 185.026755 0 0 0 0.148101 192.173711v624.167507a185.026755 185.026755 0 0 0 176.688639 192.17371H317.790598a31.76425 31.76425 0 0 0 35.734781-30.970143 210.438154 210.438154 0 0 1 21.043815-79.410624 490.757658 490.757658 0 0 1 75.837146-123.483521A500.286933 500.286933 0 0 1 556.022471 674.990306zM247.512195 154.453664h256.89337a25.014347 25.014347 0 0 1 24.22024 22.234975 28.190772 28.190772 0 0 1-23.823187 32.955409H249.497461a24.617294 24.617294 0 0 1-27.396665-25.808453 26.205506 26.205506 0 0 1 25.411399-27.793718z m-96.880961-6.749903a34.940675 34.940675 0 0 1 30.57309 17.073284 34.543622 34.543622 0 0 1 0 34.940675 34.940675 34.940675 0 0 1-30.57309 17.073284 34.543622 34.543622 0 0 1 0-69.087243z m201.305932 503.066305H140.307853a30.970143 30.970143 0 1 1 0-61.543234h211.629313a30.970143 30.970143 0 1 1 0 61.543234zM423.009675 476.463746H140.307853c-19.852656 0-35.734781-10.720434-34.940675-30.970144a31.367197 31.367197 0 0 1 34.940675-30.970143h282.701822a31.76425 31.76425 0 0 1 34.940675 30.970143 30.970143 30.970143 0 0 1-34.940675 30.970144z" fill="#c4bbf7" p-id="3286" data-spm-anchor-id="a313x.7781069.0.i1" class=""></path></svg>
                 <div style="font-size: 18px;margin-top: 10px;margin-bottom: 18px;">
                    
                     <el-tooltip class="item" effect="dark" content="查看人员画像" placement="right" style="width: 50px;display: inline;">
                        <div  @click="jumtoPersonDetail(item.id)" style="font-size: 18px;margin-top: 10px;margin-bottom: 18px;">
                            <button type="button" class="el-button el-button--danger el-button--small is-round" style="font-weight: bold;background-color:#9487dd;border-color:#9487dd">
                                <span>{{ item.personName }}</span>
                            </button>
                        </div>
                     </el-tooltip>

                </div>
            </div>

            <div class="site-info">
                <div class="site-info" style="">
                    <el-descriptions class="margin-top" :column="1" size="mini" border>
                        <el-descriptions-item  label="公司">
                            {{item.companyList[0].companyName}}
                        </el-descriptions-item>
                        <el-descriptions-item  label="行业">
                            <span v-if="item.companyList[0].industry=='' ||item.companyList[0].industry==null ">暂无</span>
                            <span v-else>{{item.companyList[0].industry}}</span>
                        </el-descriptions-item>
                        <el-descriptions-item  label="纳税识别号">
                            <span v-if="item.companyList[0].taxpayerNumber=='' ||item.companyList[0].taxpayerNumber==null ">暂无</span>
                            <span v-else>{{item.companyList[0].taxpayerNumber}}</span>
                        </el-descriptions-item>
                        <el-descriptions-item  label="公司类型">
                            <span v-if="item.companyList[0].companyType=='' ||item.companyList[0].companyType==null ">暂无</span>
                            <span v-else>{{item.companyList[0].companyType}}</span>
                        </el-descriptions-item>
                        <el-descriptions-item  label="公司状态">
                            <span v-if="item.companyList[0].companyStatus=='' ||item.companyList[0].companyStatus==null ">暂无</span>
                            <span v-else>{{item.companyList[0].companyStatus}}</span>
                        </el-descriptions-item>
                        
                        
                    </el-descriptions>
                </div>
            </div>
        </el-card>
    </div>

</template>

<script>
export default {
    data() {
        return {
            personInfoByPage:this.personInfoByPage,
        };
    },
    props:["personInfoByPage"],
    methods:{
        jumtoPersonDetail(pid){
            this.$router.push({path:"/trace/person/detail",query: {id:pid}})
        },
    },
    mounted(){
        
    },

}
</script>


<style scoped>

    .tag{
        margin-right: 10px;
        margin-bottom: 10px;
    }

  .site-card{
    margin-right: 12px !important;
    margin-bottom: 10px !important;
    margin-top: 20px;
    /*width:400px;*/
    width: 24%; /* 每个卡片占用 32% 的宽度，加上左右边距正好占用一行的宽度 */
    margin: 1%;
    border-radius:14px;
  }
    
  /* 设置网站卡片容器宽度高度*/
  .site-cards-list{
    width: 1270px;
    display: flex;
    flex-wrap: wrap;
}

::v-deep .el-card {
    margin: 0px;
  }

  /deep/ .el-descriptions-item__label.is-bordered-label {
    font-weight: bold;
    color: #909399;
    background: #fafafa;
    width: 50px;
  }

  /deep/.el-descriptions-item__content {
    word-break: break-word;
    overflow-wrap: break-word;
    width: 100px;
}

</style>

