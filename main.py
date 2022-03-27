from config import host, user, database, password, port
import psycopg2


def get_data():
    try:
        #connect to the database
        connection = psycopg2.connect(
            database = ''.join(database),
            user = ''.join(user),
            password = ''.join(password),
            host = ''.join(host),
            port = ''.join(port)
        )
        #print(host, user, database, password, port)

        with connection.cursor() as cursor:      
            cursor.execute(
                "SELECT COUNT(DISTINCT _user_id) FROM events WHERE events.event_id='3'"
                #id=3 total amount of leads
            )
            total_amount_of_leads = int(str(cursor.fetchone())[1:-2])
            print(total_amount_of_leads)

        with connection.cursor() as cursor:      
            cursor.execute(
                "SELECT SUM(CAST(amount AS float)) FROM payments"
                #total amount of revenue
            )
            total_amount_of_revenue = format(float(str(cursor.fetchone())[1:-2]),".2f")
            print(total_amount_of_revenue)

        with connection.cursor() as cursor:      
            cursor.execute(
                "SELECT COUNT(DISTINCT _user_id) FROM payments"
                #total payment amount clients
            )
            total_amount_of_UNIQUEpayed_clients = int(str(cursor.fetchone())[1:-2])
            print(total_amount_of_UNIQUEpayed_clients)
        
        with connection.cursor() as cursor:      
            cursor.execute(
                "SELECT COUNT(_user_id) FROM payments"
                #total payment amount clients
            )
            total_amount_of_payed_clients = int(str(cursor.fetchone())[1:-2])
            print(total_amount_of_payed_clients)
            
            conversion = format(total_amount_of_UNIQUEpayed_clients/total_amount_of_leads*100,".2f")
            print(conversion,"%")

           # amount_of_goods = format(total_amount_of_payed_clients/total_amount_of_UNIQUEpayed_clients,".2f")

    except Exception as _ex:
        print("[INFO] Error while working with PostgresSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Connection to PostgresSQL closed")


            
    result = dict()
    result['Общее количество заявок: '] = total_amount_of_leads
    result['Конверсия: '] = conversion
    result['Revenue: '] = total_amount_of_revenue

    return(result)