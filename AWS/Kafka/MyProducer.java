import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.IntegerSerializer;
import org.apache.kafka.common.serialization.StringSerializer;
import java.util.Properties;

public class MyProducer {
	public static void main (String[] args) {
		//step 1 - set properties
		
		//client-id or producer id, bootstrap server list, key & value serializer class
		
		Properties Producerprops = new Properties();
		Producerprops.put(ProducerConfig.CLIENT_ID_CONFIG, ConstantConfig.appID);
		Producerprops.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, ConstantConfig.bootstrapServerList);
		Producerprops.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, IntegerSerializer.class.getName());
		Producerprops.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		
		//step 2 - create object of kafka producer
		
		KafkaProducer<Integer, String> producer = new KafkaProducer<Integer, String>(Producerprops);
		
		//step 3 - calling the send method on this perticular object
		//for(int i = 1; i <50 ; i++) {
			//producer.send(new ProducerRecordInteger, String>(ConstantConfig.topicName,i,"THIS IS MY FIRST MESSAGE NUMBER "+i));
			
		//}
		
		producer.send(new ProducerRecordInteger, String>(ConstantConfig.topicName,1,"1,2013-07-25 00:00:00.0,11599,CLOSED"));
		producer.send(new ProducerRecordInteger, String>(ConstantConfig.topicName,2,"1,2013-07-25 00:00:00.0,11599,COMPLETE"));
		
		//step 4 - close the producer object
		
		producer.close();
		
	}
	
}
		
		
		
		