pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mourya26/trusturl"
        DOCKER_TAG   = "latest"
        CONTAINER_NAME = "trusturl-container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/mourya26/TrustURL.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKER_IMAGE%:%DOCKER_TAG% ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                    bat "docker push %DOCKER_IMAGE%:%DOCKER_TAG%"
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    // Stop and remove old container without failing the build if it doesn't exist
                    bat "docker ps -q -f name=%CONTAINER_NAME% && docker stop %CONTAINER_NAME%"
                    bat "docker ps -a -q -f name=%CONTAINER_NAME% && docker rm %CONTAINER_NAME%"
                    bat "docker run -d --name %CONTAINER_NAME% -p 5000:5000 %DOCKER_IMAGE%:%DOCKER_TAG%"
                }
            }
        }
    }
}
