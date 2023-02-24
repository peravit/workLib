import pandas as pd
import datetime as dt
from getFiles import load_data

def prep_data(data):
    stop_word = ["บริษัท หลักทรัพย์ ลิเบอเรเตอร์ จำกัด\r\n.\r\nเปิดให้ใช้งานอย่างเต็มรูปแบบในวันที่ 3 มกราคม 2566 \r\nและให้บริการซื้อขายหลักทรัพย์ผ่านแอปพลิเคชั่น ‘Liberator’ เพียงช่องทางเดียวเท่านั้น\r\n.\r\nดาวน์โหลดแอปพลิเคชั่นพร้อมสมัครเปิดบัญชี ได้เลยตอนนี้ ทั้ง iOS และ Android ที่ คลิ๊ก > https://onelink.to/fp5n58 \r\n\r\nแล้วมาสัมผัสประสบการณ์เทรดหุ้น 0% ครั้งแรกของไทย ไปด้วยกัน Liberator #โลกลงทุนที่ทุกคนเท่ากัน",
             'ขอบคุณครับ', 
             'ครับ', 
             'คุณส่งรูป', 
             'คุณส่งสติกเกอร์',  
             'ประกาศต่างๆ ที่เกี่ยวกับค่าธรรมเนียมและขั้นตอนการทำธุรกรรมต่างๆ สามารถดูได้ที่ https://www.liberator.co.th/announcement/\r\n\r\n\r\nแล้วมาสัมผัสประสบการณ์เทรดหุ้น 0% ครั้งแรกของไทย ไปด้วยกัน Liberator #โลกลงทุนที่ทุกคนเท่ากัน\r\n\r\n\r\
                nดาวน์โหลดแอปพลิเคชั่นพร้อมสมัครเปิดบัญชี ได้เลยตอนนี้ ทั้ง iOS และ Android ที่ คลิ๊ก > https://onelink.to/fp5n58', 
            'Buttons alt text', 
            'คุณลูกค้าอยากคุยกับพี่แอดมิน น้อง Chatbot ขอไปตามพี่แอดมินมาตอบ โปรดรอสักครู่นะคะ :)\r\nเพื่อความสะดวกรวดเร็ว คุณลูกค้าสามารถแจ้งเรื่องที่ต้องการติดต่อ ชื่อ-นามสกุล และเบอร์ติดต่อของลูกค้าได้เลยค่ะ',
            'ใช่ครับ',
            'กรุณารอสักครู่ จะทำการแจ้งให้แอดมินมาตอบนะคะ หรือกดปุ่มติดต่อแอดมินด้านล่างเพื่อติดต่อทันที',
            'ยินดีค่ะ',
            '1.บัตรประชาชน\r\n\r\n2.เอกสารหน้าBookBank\r\n\r\n3.เอกสารแสดงทางการเงิน เช่น Slipเงินเดือน Statementอัพเดทย้อนหลัง3เดือน กรณีลูกค้าขอวงเงินบัญชี Cash Balance มากกว่า 500,000 หรือเปิดบัญชี Cash และ Tfex\r\n\r\n4.การ์ดลายเซ็น (เซ็นในเอกสารเปล่า)',
            'ขอบคุณค่ะ',
            'สวัสดีครับ',
            'คุณลูกค้าอยากคุยกับพี่แอดมิน น้อง Chatbot ขอไปตามพี่แอดมินมาตอบ โปรดรอสักครู่นะคะ :)\r\n\r\nเพื่อความสะดวกรวดเร็ว คุณลูกค้าสามารถแจ้งเรื่องที่ต้องการติดต่อ ชื่อ-นามสกุล และเบอร์ติดต่อของลูกค้าได้เลยค่ะ',
            'ลูกค้าสามารถเปิดบัญชีกับทางLiberatorได้จากทางหน้า Application\r\nโดยลูกค้าสามารถดาวน์โหลด Application ผ่านทาง\r\nhttps://onelink.to/fp5n58\r\n\r\nโดยลูกค้าสามารถโหลดคู่มือการสมัครได้ผ่านทาง\r\nhttps://drive.google.com/file/d/1HIZMRqW5e5UMIHWFGmzTeUkZXP0OHmzG/view?usp=share_link\r\n',
             'ค่ะ',
             'โอเคค่ะ',
             'ใช่ค่ะ',
             'ครับผม',
             'ได้ครับ'
             ]
    #df = load_data()
    df = data
    ## exclude stop word
    df = df[df['ข้อความ'].map(lambda x: str(x) not in stop_word)]

    def f(row):
        if row['ประเภทผู้ส่ง'] == 'Account' and row['ชื่อผู้ส่ง'] != 'ข้อความตอบกลับอัตโนมัติ'and row['ชื่อผู้ส่ง'] !='Unknown':
            val = 'Agent'
        elif row['ประเภทผู้ส่ง'] == 'Account' and row['ชื่อผู้ส่ง'] == 'ข้อความตอบกลับอัตโนมัติ':
            val = 'Auto-response'
        elif row['ประเภทผู้ส่ง'] == 'Account' and row['ชื่อผู้ส่ง'] == 'Unknown':
            val = 'line_bot'
        elif row['ประเภทผู้ส่ง'] == 'User':
            val = 'User'
        return val

    def f2(row):
        if row['ประเภทผู้ส่ง'] == 'Account' and row['ชื่อผู้ส่ง'] != 'ข้อความตอบกลับอัตโนมัติ'and row['ชื่อผู้ส่ง'] !='Unknown':
            val = row['ชื่อผู้ส่ง']
        else:
            val = '-'
        return val
    ## condituon cols
    df['Sender_name'] = df.apply(f, axis=1)
    df['Agent_name'] = df.apply(f2, axis=1)
    df['Datetime'] = pd.to_datetime(df['วันส่ง']).dt.strftime('%d/%m/%Y') +','+' '+ df['เวลาส่ง']
    # drop mun
    df = df.drop('ชื่อผู้ส่ง', axis=1)
    # Change order columns & rename cols
    df = df[['chat_name',  'วันส่ง', 'เวลาส่ง', 'ประเภทผู้ส่ง', 'Sender_name', 'Agent_name', 'ข้อความ', 'Datetime']]
    df.columns = ['chat_name', 'Date', 'Time', 'sender_type', 'Sender_name', 'Agent_name', 'messages', "Datetime"]

    return df