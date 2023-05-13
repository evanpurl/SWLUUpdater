pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Deliver') { 
            agent any
            environment { 
                VOLUME = '$PWD/sources:/src'
                IMAGE = 'cdrx/pyinstaller-windows:python3'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller main.py --noconsole --onefile --icon=purlsicon.ico --name SWLU-Updater'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/SWLU-Updater.exe"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}
