pipeline {
    agent { label 'jenkins-agent' }

    environment {
        ARTIFACT_PATH = "/home/jenkins/artifacts"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'dev', url: 'https://github.com/Imma016/flask-app-cicd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    if ! command -v pip &> /dev/null
                    then
                        echo "pip not found, installing..."
                        sudo apt-get update
                        sudo apt-get install -y python3 python3-pip
                        sudo ln -sf /usr/bin/pip3 /usr/bin/pip
                    fi

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
                    ansible-playbook -i inventory deploy.yml
                '''
            }
        }
    }
}

