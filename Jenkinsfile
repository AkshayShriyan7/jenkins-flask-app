pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sample-jenkins-flask-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AkshayShriyan7/jenkins-flask-app.git'
            }
        }

	  stage('Install Python and Pip') {
            steps {
                sh '''
                # Install Python and pip
                sudo apt-get update
                sudo apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Deploy Locally') {
            steps {
                script {
                    // Use docker-compose to bring down any existing containers and redeploy the new Flask app locally
                    sh 'docker-compose down'
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }

}

