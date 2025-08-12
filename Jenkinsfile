pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mourya26/trusturl"   // Your Docker Hub repo name
        DOCKER_TAG   = "latest"
        CONTAINER_NAME = "trusturl-container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/mourya26/TrustURL.git'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKER_IMAGE%:%DOCKER_TAG% ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat "docker push %DOCKER_IMAGE%:%DOCKER_TAG%"
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    bat "docker stop %CONTAINER_NAME% || exit 0"
                    bat "docker rm %CONTAINER_NAME% || exit 0"
                    bat "docker run -d --name %CONTAINER_NAME% -p 5000:5000 %DOCKER_IMAGE%:%DOCKER_TAG%"
                }
            }
        }
    }
}
