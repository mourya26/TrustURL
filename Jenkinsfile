pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mourya26/trusturl"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/mourya26/TrustURL.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                    bat 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    bat 'docker rm -f trusturl || true'
                    bat 'docker run -d --name trusturl -p 5000:5000 $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }
    }
}
