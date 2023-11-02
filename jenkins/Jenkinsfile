pipeline {
    agent any

    // environment {
    //     TOKEN     = credentials('clo')
    //
    // }
    parameters {
          string(
           name: 'BRANCH',
           defaultValue: 'feature/init',
           description: 'BRANCH'
         )


         }

   stages() {
     stage('SCM') {
       steps {
         script{
           checkout([$class: 'GitSCM', branches: [[name: BRANCH]],
              doGenerateSubmoduleConfigurations: false,
              extensions: [[$class: 'RelativeTargetDirectory',
              relativeTargetDir: 'app/']], gitTool: 'Default',
              submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'ssh-git',
              url: 'git@github.com:RoboInterativo/robomath.git']]])
              sh 'zip app.zip app -r'
              sh 'mv app.zip ansible/files'

         }

       }

     }
     stage('Test1' ) {
       steps {
         script {
           sh """
           echo HELLO
           pwd
           ls -li
           """
           ansiblePlaybook extras: "-vv -u root --extra-vars \" inventory_dir=\"${WORKSPACE}/ansible/inventories/dev/\"\" ",
                         installation: 'ansible29',
                         inventory: "ansible/inventories/dev/inventory",
                         playbook: "ansible/test.yaml"


         }
        }
      }
   }
   post {
       success {

           archiveArtifacts allowEmptyArchive: true, artifacts: '${WORKSPACE}/simple-back-front/front/*.zip', fingerprint: true

       }
     }

 }
