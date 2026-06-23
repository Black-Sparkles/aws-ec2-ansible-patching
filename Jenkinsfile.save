pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out repository...'
                checkout scm
            }
        }

        stage('Verify Ansible') {
            steps {
                sh 'ansible --version'
            }
        }

        stage('Pre-Patch Validation') {
            steps {
                sh 'ansible-playbook -i inventories/hosts.ini playbooks/check-services.yml'
            }
        }

        stage('Run Rolling Patching') {
            steps {
                sh 'ansible-playbook -i inventories/hosts.ini playbooks/rolling-patch.yml'
            }
        }

        stage('Post-Patch Validation') {
            steps {
                sh 'ansible-playbook -i inventories/hosts.ini playbooks/check-services.yml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.txt', allowEmptyArchive: true
        }

        success {
            echo 'Patching completed successfully.'
        }

        failure {
            echo 'Patching failed. Review Jenkins logs and patch reports.'
        }
    }
}
