FROM registry.access.redhat.com/ubi8/ubi:8.0
ADD info.sh /tmp
CMD /tmp/info.sh
CMD bash -c "while true; do (( i++ )); echo test-kush \$i; slepp 5; done"
