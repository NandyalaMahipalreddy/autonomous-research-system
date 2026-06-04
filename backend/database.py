import sqlite3

DB_NAME = "research_history.db"


def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS research_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        query TEXT,
        report TEXT,
        cost REAL,
        pdf_file TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_research(
    query,
    report,
    cost,
    pdf_file
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO research_history
        (
            query,
            report,
            cost,
            pdf_file
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            query,
            report,
            cost,
            pdf_file
        )
    )

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        query,
        cost,
        pdf_file,
        created_at
    FROM research_history
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_report(report_id):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT report
        FROM research_history
        WHERE id = ?
        """,
        (report_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row[0] if row else ""


def delete_research(research_id):

    conn = sqlite3.connect(
        "research_history.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM research_history WHERE id=?",
        (research_id,)
    )

    conn.commit()

    conn.close()