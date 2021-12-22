out_folder="/home/<user>/triptico/tripticoEdge"
sshpass -p <password> sftp -r -o ConnectTimeout=10 <username>@<ip>:<url><<< $"put '$out_folder'" && rm -rf $out_folder/* && mkdir $out_folder/RPiIMU $out_folder/RPiIMU2 $out_folder/RPiFotos $out_folder/RPiREC
