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
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                    sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    sh 'docker rm -f trusturl || true'
                    sh 'docker run -d --name trusturl -p 5000:5000 $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }
    }
}
