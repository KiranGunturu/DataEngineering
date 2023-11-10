import org.apache.hadoop.fs.Path;

val source_table = "drba_ada_dealer_t"
val target_table = "ada_dealer_t" 
val partition_number = 1
val database = "nna_tcs_bde_dads"
// Path for the sample data and the entire dataset
val output_path = s"/user/allzeppelindocs/NNA_TCS_BDE_DADS/00_data/EpsilonEconomics/$target_table"
val df = spark.sql(s"SELECT * FROM $database.$source_table")

/*** ORIGINAL DATASET ***/
println("RECORD COUNT: " + df.count)
println("FIELDS COUNT: " + df.columns.size)
df.printSchema

/*** MODIFIED DATASET ***/
val affirmativeFields = Seq( 
"DEALER_NO",
"CLASS_OF_DEALER_CD",
"DEALER_FCLTY_ADDR_2",
"DEALER_FCLTY_ADDR_4",
"DEALER_FCLTY_CITY_ST_1",
"DEALER_FCLTY_CITY_ST_2",
"DEALER_FCLTY_NM",
"DEALER_FCLTY_ZIP_CD",
"RGN_CD",
"SVC_DSTRCT_CD",
"APPOINT_DT",
"DEALER_STATUS_CD",
"SLS_POINT_NO",
"CHANNEL_ELIG_CD",
"UNITS_IN_OPER_QT"
)
val uncertainFields = Seq(
"ADVER_CD",
"AGMT_ACT_DT",
"AGMT_ACT_SECT_CD",
"AGMT_EXPIR_DT",
"AGMT_TYPE_CD",
"AUTO_TERMS_CD",
"CMO_GROUP_CD",
"EXTND_SRV_IN",
"MKT_GUIDE_CAR_TRUCK_CD",
"OWN_TYPE_CD",
"PREV_WARR_LABOR_RATE",
"SVC_PDC_CD",
"STATE_CD",
"TERM_TYP_CD",
"TERM_DT",
"WARR_LABOR_RATE",
"PARTS_TERM_CD",
"MK_CRTFD_1_CD",
"MK_CRTFD_2_CD",
"MK_CRTFD_3_CD",
"MK_CRTFD_4_CD",
"MK_CRTFD_5_CD",
"MK_CRTFD_6_CD",
"MK_CRTFD_7_CD",
"MK_CRTFD_8_CD",
"MK_CRTFD_9_CD",
"MK_CRTFD_10_CD"
)

val allFields = affirmativeFields ++ uncertainFields

val withRequiredColumnsDf = df.select(allFields.map(col):_*)

println("RECORD COUNT: " + withRequiredColumnsDf.count)
println("FIELDS COUNT: " + withRequiredColumnsDf.columns.size)
withRequiredColumnsDf.printSchema

/*** SAMPLE DATA 
val df_sample = spark.sql(s"SELECT * FROM $database.$source_table LIMIT 1000").select(allFields.map(col):_*)
df_sample.repartition(1).write.format("csv").mode("overwrite").option("header","true").option("compression","gzip").save(output_path)
df_sample.show***/

// DESCRIBE FORMATTED ORIGINAL DATA 
val table_location = spark.sql(s"DESCRIBE FORMATTED $database.$source_table").filter("col_name='Location'").collect()(0).getString(1)
val hdfs_path = new Path(table_location)
val fs = hdfs_path.getFileSystem(spark.sparkContext.hadoopConfiguration)
// SIZE IN GBs
println("Size: " + fs.getContentSummary(hdfs_path).getLength.toLong/1e9 + " GB")
// FILE LISTING
fs.listStatus(hdfs_path).foreach( x => println(x.getPath + "  " + x.getLen.toLong/1e6 + " MB")  ) 

/*** DESCRIBE MODIFIED DATA ***/
// val partition_number = 2
 withRequiredColumnsDf.repartition(partition_number).write.format("csv").mode("overwrite").option("header","true").option("compression","gzip").save(output_path)
 
 
 
 val hdfs_path = new Path(output_path)
 val hdfs = hdfs_path.getFileSystem(spark.sparkContext.hadoopConfiguration)

// SIZE IN GBs
 println("Size: " + hdfs.getContentSummary(hdfs_path).getLength.toLong/1e9 + " GB")

// FILE LISTING
 hdfs.listStatus(hdfs_path).foreach( x => println(x.getPath + "  " + x.getLen.toLong/1e6 + " MB")  )
 
 import org.apache.hadoop.fs.{FileStatus, FileSystem, Path}

def renameFile(original: String ): String ={
    if (original.contains("part-")){
        val prefix = original.substring(0, original.indexOf("part-"))
        val table = prefix.split("/").toList.last
        val suffix = original.substring(original.indexOf("part-"), original.length)
        val part = suffix.split("-").toList(1)
        return "%s%s%s.csv.gz".format(prefix, table, part)
    } else{
        return original
    }
}

//val target_table = "ada_dealer_t"
// Path for the sample data and the entire dataset
val output_path = s"/user/allzeppelindocs/NNA_TCS_BDE_DADS/00_data/EpsilonEconomics/$target_table"
val hdfs_path = new Path(output_path)
val fs = hdfs_path.getFileSystem(spark.sparkContext.hadoopConfiguration)

// FILE RENAMING
fs.listStatus(hdfs_path) // Array[FileStatus]         
.map( path => (path.getPath, renameFile(path.getPath.toString))) // Array[(Path, String)]
.map( pair => (pair._1, new Path(pair._2))) // Array[(Path, Path)]
.map( paths => fs.rename(paths._1, paths._2)) // Unit

## Data Offloading

import org.apache.hadoop.fs.Path;

val source_hdfs_file = s"hdfs://bdeprd/user/allzeppelindocs/NNA_TCS_BDE_DADS/00_data/EpsilonEconomics/$target_table/"
val hdfs_path = new Path(source_hdfs_file)
val hdfs = hdfs_path.getFileSystem(spark.sparkContext.hadoopConfiguration)

//val target_local_file = s"/tmp/epsilon/drba"

val target_local_file = s"/data/1/projects/nna_tcs_bde_dads/data/arc/epsilon/drba"
val local_path = new Path(target_local_file)
hdfs.copyToLocalFile(hdfs_path, local_path)

%sh
ls -ltr /data/1/projects/nna_tcs_bde_dads/data/arc/epsilon/drba/ada_dealer_t

%sh
for file in /data/1/projects/nna_tcs_bde_dads/data/arc/epsilon/drba/ada_dealer_t/*.gz ; do gpg --encrypt --recipient "PSN2QUALITY_PROD20220316 <ISEFTPPGPAdminSystem@>" --trust-model always $file; done
#rm /tmp/epsilon/drba/svc_wol_comn_t/*.csv.gz
#ls -lR /tmp/epsilon/drba

%sh
ls /data/1/data//*

import java.io.{File, FileInputStream, IOException, InputStream, OutputStream}
import org.apache.commons.net.ftp.{FTPClient, FTPClientConfig, FTPReply, FTP}


def createFTPClient(/*server_url: String , user: String, pass:, int type */): FTPClient = {
    
    val server_url= "hosyz"
    val username= "test"
    val password= "password"
    val target_directory = "folder"
    
    val ftp: FTPClient = new FTPClient();
    val conf: FTPClientConfig = new FTPClientConfig(FTPClientConfig.SYST_UNIX);
    ftp.configure(conf); // conf.setServerLanguageCode("en");
    ftp.connect(server_url)
    // attempt to login
    if (!ftp.login(username, password)) {
        println("Failed to login to FTP")
        ftp.disconnect();
    }
    // ftp.enterLocalPassiveMode()
    if (! ftp.setFileType( FTP.BINARY_FILE_TYPE )) {
        //throw new Exception("Failed to set ftpClient object to BINARY_FILE_TYPE");
        println("Failed to set ftpClient object to BINARY_FILE_TYPE");
    }
    // check for successful connection
    if (!FTPReply.isPositiveCompletion(ftp.getReplyCode)) {
        ftp.disconnect();
        //throw new Exception("Failed to connect properly to FTP");
        println("Failed to connect properly to FTP");
    }
    // Success! return connected MyFTPClient.
    //println("Successfully connected to " + server + ". " + ftpClient.getReplyString) // 230 FTP Response code. User logged in, proceed.
    return ftp;
}

val ftpClient = createFTPClient()

/*** LISTING FTP DIRECTORY CONTENT ***/
//ftpClient.listFiles("./outbound/").toList.foreach( file => println(file/*.getName*/))

import java.io.{File, FileInputStream, IOException, InputStream, OutputStream, FilenameFilter}

val dir: File = new File("/data/1//");

val allFiles = dir.listFiles(new FilenameFilter {
        override def accept(dir: File, name: String): Boolean = {
          name.endsWith(".gz.gpg")
        }
      })

allFiles.foreach( file => {
    println(s"./outbound/EpsilonEconomics/${file.getName}")
    val inputStream: InputStream  = new FileInputStream(file);
    ftpClient.storeFile(s"./outbound/EpsilonEconomics/${file.getName}", inputStream)
})

ftpClient.listFiles("./outboun").toList.foreach( file => println(file))


