pipeline {
    agent { label 'jenkins-agent' }

    environment {
        ARTIFACT_PATH = "/home/jenkins/artifacts"
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'dev', url: 'https://github.com/Imma016/flask-app-cicd.git'
            }
        }

        stage('Setup Python Virtualenv') {
            steps {
                sh '''
                    set -e
                    sudo apt-get update -qq
                    sudo apt-get install -y python3-venv python3-full ansible

                    python3 -m venv venv
                    . venv/bin/activate

                    pip install --upgrade pip
                    pip install -r app/requirements.txt
                '''
            }
        }

        stage('Build & Package') {
            steps {
                sh '''
                    tar -czvf flask-app.tar.gz app/
                '''
            }
        }

        stage('Archive Artifact') {
            steps {
                sh '''
                    mkdir -p "$ARTIFACT_PATH"
                    mv flask-app.tar.gz "$ARTIFACT_PATH"
                '''
            }
        }

        stage('Trigger Ansible Deployment') {
            steps {
                sh '''
                    cd ansible
                    ansible-playbook -i inventory deploy.yml
                '''
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed! Check the logs for details.'
        }
        success {
            echo 'Pipeline succeeded! Deployment complete.'
        }
    }
}
