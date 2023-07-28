import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.IntegerSerializer;
import org.apache.kafka.common.serialization.StringSerializer;
import java.util.Properties;

public class MyConsumer {
	public static void main(String[] args) {
		
		//set properties
		
		Properties consumerProps = new Properties();
		consumerProps.put(ConsumerConfig.CLIENT_ID_CONFIG, ConstantConfig.appID);
		consumerProps.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, ConstantConfig.bootstrapServerList);
		consumerProps.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, IntegerDeserializer.class);
		consumerProps.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
		consumerProps.put(ConsumerConfig.GROUP_ID_CONFIG, "CONSUMER_GROUP1");
		consumerProps.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
		
		//Consumer object and assign the properties
		
		KafkaConsumer<Integer, String> Consumer = new KafkaConsumer<Integer, String>(consumerProps);
		
		// subscribe to the list of topics
		
		consumer.subscribe(Arrays.asList("all_orders_topic"));
		
		//create a producer and write to it after consuming
		
		Properties Producerprops = new Properties();
		
		Producerprops.put(ProducerConfig.CLIENT_ID_CONFIG, ConstantConfig.appID);
		Producerprops.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, ConstantConfig.bootstrapServerList);
		Producerprops.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, IntegerDeserializer.class);
		Producerprops.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringDeserializer.class);
		
		//Kafka Producer Object
		
		KafkaProducer<Integer, String> producer = new KafkaProducer<Integer, String>(Producerprops);
		
		// pull for every 100 ms
		
		while(true) {
			
			ConsumerRecords<Integer, String> records = consumer.poll(100);
			
			for (ConsumerRecord<Integer, String> record: records) {
				
				if(record.value().split(",")[3].equals("CLOSED"))
				{
					producer.send(new ProducerRecord<Integer, String>("closed_orders",record.key(), record.value()));
				}
				else
				{
					producer.send(new ProducerRecord<Integer, String>("completed_orders",record.key(), record.value()));
				}
			}
		}
		
	}
	
}
		