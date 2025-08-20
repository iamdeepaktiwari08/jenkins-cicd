pipeline {
    agent any

    environment {
        IMAGE_NAME = "mywebapp"
        CONTAINER_NAME = "mywebapp-container"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo "📥 Cloning Repository..."
                git branch: 'main', url: 'https://github.com/iamdeepaktiwari08/jenkins-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker Image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo "🛑 Stopping old container..."
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                echo "🚀 Running new container..."
                sh 'docker run -d --name $CONTAINER_NAME -p 81:80 $IMAGE_NAME'
            }
        }

        stage('Test Deployment') {
            steps {
                echo "🔍 Testing Deployment..."
                sh 'curl -s http://localhost:81 | grep "Jai Shri Ram"'
            }
        }
    }
}
