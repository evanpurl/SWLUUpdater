pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Deliver') { 
            agent any
            environment { 
                VOLUME = '$PWD/sources:/src cdrx/pyinstaller-windows:python3'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    sh "docker run --rm -v ${VOLUME} 'pyinstaller -F main.py --noconsole --onefile --icon=purlsicon.ico --name SWLU-Updater'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/dist/SWLU-Updater.exe"
                }
            }
        }
    }
}
