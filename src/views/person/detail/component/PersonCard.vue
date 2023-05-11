<template>
    <el-card style="margin-bottom:20px;">
      <div slot="header" class="clearfix">
        <span>About Him</span>
      </div>
  
      <div class="user-profile">
        <div class="box-center">
          <pan-thumb :image="avatar" :height="'100px'" :width="'100px'" :hoverable="false"></pan-thumb>
        </div>
        <div class="box-center">
          <div class="user-name text-center">{{ personInfo.personName }}</div>
          <!-- <div class="user-role text-center text-muted">{{ user.role | uppercaseFirst }}</div> -->
        </div>
      </div>
  
      <div class="user-bio">
        <div class="user-education user-bio-section">
          <div class="user-bio-section-header"><svg-icon icon-class="education" /><span>纳税人识别号</span></div>
          <div class="user-bio-section-body">
            <div class="text-muted">
              <span v-if="personInfo.companyList==undefined || personInfo.companyList[0].taxpayerNumber=='' ||personInfo.companyList[0].taxpayerNumber==null ">暂无</span>
              <span v-else>{{personInfo.companyList[0].taxpayerNumber}}</span>
            </div>
          </div>
        </div>
  
        <div class="user-skills user-bio-section">
          <div class="user-bio-section-header"><svg-icon icon-class="skill" /><span>旗下网站</span></div>
          <div class="user-bio-section-body">   
                <!-- <el-alert

                type="warning"
                effect="dark"
                description="该人员存在被检测为恶意的下载网站"
                show-icon></el-alert> -->
            <div class="progress-item">
              <span>恶意下载网站</span>
              <!-- <el-progress :percentage="malSite" color="#F56C6C"/> -->
              <el-progress percentage=100 color="#F56C6C"/>
            </div>
            <div class="progress-item">
              <span>正常下载网站</span>
              <!-- <el-progress :percentage="goodSite" /> -->
              <el-progress percentage=0 />
            </div>

          </div>
        </div>
      </div>
    </el-card>
  </template>
  
  <script>
  import PanThumb from '@/components/PanThumb'
  import img from'@/assets/nodes/people1.png'

  export default {
    components: { PanThumb },
    props:["personInfo"],
    data(){
        return{
            avatar:img,
            goodSite:'',
            malSite:'',
        }
    },
    watch: {
        personInfo(newVal,oldVal) {
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
  