MERGE
       INTO  tgt_tbl tgt
      USING  src_tbl src
         ON  ( src.id = tgt.id ) 
       WHEN MATCHED 
       THEN
     UPDATE
        SET   tgt.name = src.fname,
              tgt.lname = src.lname
	--  WHERE clause if needed
       WHEN NOT MATCHED                         
       THEN
     INSERT ( tgt.id,                   
              tgt.fname,
              tgt.lname )
     VALUES ( src.id,
              src.fname,
              src.lname );
			  

