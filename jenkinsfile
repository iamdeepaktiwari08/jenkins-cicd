pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo "📥 Cloning Repository..."
                git 'https://github.com/iamdeepaktiwari08/jenkins-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker Image..."
                sh 'docker build -t webapp:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo "🛑 Stopping old container if exists..."
                sh '''
                if [ $(docker ps -q -f name=webapp) ]; then
                    docker stop webapp && docker rm webapp
                fi
                '''
            }
        }

        stage('Run New Container') {
            steps {
                echo "🚀 Running New Container on port 81..."
                sh 'docker run -d --name webapp -p 81:80 webapp:latest'
            }
        }

        stage('Test Deployment') {
            steps {
                echo "🔍 Testing Deployment..."
                sh 'curl -I http://192.168.77.137:81 || exit 1'
            }
        }
    }
}
