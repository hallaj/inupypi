pipeline {
  agent none
  stages {
    stage('Build') {
      steps {
        sh 'nosetests -sv tests'
      }
    }
  }
}