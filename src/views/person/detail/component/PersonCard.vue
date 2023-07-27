<template>
    <el-card style="margin-bottom:20px;"  body-style="height:520px;width:300.7px;"                     v-loading="loading"
    element-loading-text="Loading"
    element-loading-spinner="el-icon-loading"
    element-loading-background="#343A40" >
      <div slot="header" class="clearfix">
        <span style="font-family:Times New Roman;font-size:medium">About Him</span>
      </div>
  
      <div class="user-profile">
        <div class="box-center">
          <pan-thumb :image="avatar" :height="'100px'" :width="'100px'" :hoverable="false"></pan-thumb>
        </div>
        <div class="box-center">
          <div class="user-name text-center" style="font-family:Times New Roman;font-size:medium">{{ pinyin.getFullChars(personInfo.personName) }}</div>
        </div>
      </div>
  
      <div class="user-bio">
        <div class="user-education user-bio-section">
          <div class="user-bio-section-header"><svg-icon icon-class="education" /><span>纳税人识别号</span></div>
          <div class="user-bio-section-body">
            <div class="text-muted">
              <span v-if="personInfo.companyList==undefined || personInfo.companyList[0].taxpayerNumber=='' ||personInfo.companyList[0].taxpayerNumber==null ">暂无</span>
              <span v-else style="font-family:Times New Roman;font-size:medium">{{personInfo.companyList[0].taxpayerNumber}}</span>
            </div>
          </div>
        </div>
  
        <div class="user-skills user-bio-section">
          <div class="user-bio-section-header">
            <svg-icon icon-class="skill" /><span>信用情况</span>
            <i v-if="malSite>0" class="el-icon-warning" style="margin-left:110px;font-size: 14px;color: #E6A23C;"> 存在风险</i>
            <i v-if="malSite==0" class="el-icon-success" style="margin-left:110px;font-size: 14px;color:#67C23A;"> 信用正常</i>
          </div>
          <div class="user-bio-section-body">   
            <div class="progress-item">
              <el-row style="margin-top:20px;">
                <el-col :span="8" style="margin-bottom:15px;"><a-tag  color="#F56C6C">恶意网站：</a-tag></el-col>
                <el-col :span="16"><el-progress :percentage="malSite" color="#F56C6C"/></el-col>
              </el-row>
            </div>
            <div class="progress-item">
              <el-row>
                <el-col :span="8"  style="margin-bottom:15px;"><a-tag  color="#1AABA8">正常网站：</a-tag></el-col>
                <el-col :span="16"><el-progress :percentage="goodSite" /></el-col>
              </el-row>
            </div>

          </div>
        </div>
      </div>
    </el-card>
  </template>
  
  <script>
  import PanThumb from '@/components/PanThumb'
  import img from'@/assets/nodes/people1.png'
  let pinyin = require('js-pinyin');
  pinyin.setOptions({checkPolyphone: false, charCase: 0});

  export default {
    components: { PanThumb },
    props:["personInfo"],
    data(){
        return{
            loading:true,
            avatar:img,
            goodSite:'',
            malSite:'',
            pinyin:pinyin,
        }
    },
    watch: {
        personInfo(newVal,oldVal) {
            this.loading=false;
            this.countSite()
        },
    },
    methods:{

        countSite(){
            const allSiteCount = this.personInfo.companyList[0].siteList.length;
            var malSiteCount = 0;
            var goodSiteCount = 0;
            for(var site in this.personInfo.companyList[0].siteList){
                if(site.isMalicious==true){
                    goodSiteCount+=1;
                }else{
                    malSiteCount+=1;
                }
            }
            this.goodSite=goodSiteCount/allSiteCount*100;
            this.malSite=malSiteCount/allSiteCount*100;
            console.log("good",goodSiteCount,"mal",malSiteCount,"all",allSiteCount);
        }
    },
    

  }
  </script>
  
  <style lang="scss" scoped>
  .box-center {
    margin: 0 auto;
    display: table;
  }
  
  .text-muted {
    color: #777;
  }
  
  .user-profile {
    margin-top:30px;
    margin-bottom: 30px;
    .user-name {
      font-weight: bold;
    }
  
    .box-center {
      padding-top: 10px;
    }
  
    .user-role {
      padding-top: 10px;
      font-weight: 400;
      font-size: 14px;
    }
  
    .box-social {
      padding-top: 30px;
  
      .el-table {
        border-top: 1px solid #dfe6ec;
      }
    }
  
    .user-follow {
      padding-top: 20px;
    }
  }
  
  .user-bio {
    margin-top: 20px;
    margin-bottom: 30px;;
    span {
      padding-left: 4px;
    }
  
    .user-bio-section {
      font-size: 14px;
      padding: 15px 0;
  
      .user-bio-section-header {
        border-bottom: 1px solid #dfe6ec;
        padding-bottom: 10px;
        margin-bottom: 10px;
        font-weight: bold;
      }
    }
  }

  </style>

<style scoped>
  /deep/.el-progress {
    width: 180px;
  }
</style>