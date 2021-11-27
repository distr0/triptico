#!/bin/bash
sshpass -p <password> sftp -o ConnectTimeout=10 <username>@<ip>:/triptico/tripticoEdge/RPiIMU <<< $"put '$1'"
