docker run -d -p 8081:8081 -p 8082:8082 --name nexus -v nexus-data:/nexus-data sonatype/nexus3

curl -u 'admin:Sewy1324@#' http://localhost:8081/service/rest/v1/system/eula

DISCLAIMER=$(curl -s -u 'admin:Sewy1324@#' http://localhost:8081/service/rest/v1/system/eula | jq -r .disclaimer)

curl -X POST -u 'admin:Sewy1324@#' -H "Content-Type: application/json" http://localhost:8081/service/rest/v1/system/eula -d "{\"accepted\":true,\"disclaimer\":\"$DISCLAIMER\"}"