import csv
import statistics

def analyze_student_scores(csv_file):
    """
    CSVファイルから学生の成績データを読み込み、各参加者の統計情報を算出する
    
    Args:
        csv_file (str): CSVファイルのパス
    
    Returns:
        dict: 各学生の統計情報
    """
    try:
        # CSVファイルを読み込む
        data = []
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    '名前': row['名前'],
                    '日付': row['日付'],
                    '科目': row['科目'],
                    'スコア': int(row['スコア'])
                })
        
        # データの確認
        students = list(set(row['名前'] for row in data))
        subjects = list(set(row['科目'] for row in data))
        dates = [row['日付'] for row in data]
        
        print("=== データの概要 ===")
        print(f"総データ数: {len(data)}件")
        print(f"参加者数: {len(students)}人")
        print(f"科目数: {len(subjects)}科目")
        print(f"対象期間: {min(dates)} ～ {max(dates)}")
        print()
        
        # 各参加者の統計情報を算出
        results = {}
        
        for student in students:
            student_scores = [row['スコア'] for row in data if row['名前'] == student]
            
            results[student] = {
                '平均点': round(statistics.mean(student_scores), 2),
                '最高点': max(student_scores),
                '最低点': min(student_scores),
                'テスト回数': len(student_scores),
                'スコア詳細': student_scores
            }
        
        return results
    
    except FileNotFoundError:
        print(f"エラー: ファイル '{csv_file}' が見つかりません。")
        return None
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None

def display_results(results):
    """
    分析結果を分かりやすく表示する
    
    Args:
        results (dict): 各学生の統計情報
    """
    if not results:
        return
    
    print("=" * 60)
    print("           📊 学生成績分析結果 📊")
    print("=" * 60)
    
    # 各学生の結果を表示
    for i, (student, stats) in enumerate(results.items(), 1):
        print(f"\n【{i}. {student}】")
        print(f"   📈 平均点:     {stats['平均点']:6.2f}点")
        print(f"   🏆 最高点:     {stats['最高点']:6d}点")
        print(f"   📉 最低点:     {stats['最低点']:6d}点")
        print(f"   📝 テスト回数: {stats['テスト回数']:6d}回")
        print(f"   📋 スコア詳細: {stats['スコア詳細']}")
        print("-" * 50)
    
    # 全体統計
    all_averages = [stats['平均点'] for stats in results.values()]
    all_max_scores = [stats['最高点'] for stats in results.values()]
    all_min_scores = [stats['最低点'] for stats in results.values()]
    
    print("\n🌟 全体統計")
    print(f"   クラス平均:     {statistics.mean(all_averages):6.2f}点")
    print(f"   クラス最高点:   {max(all_max_scores):6d}点")
    print(f"   クラス最低点:   {min(all_min_scores):6d}点")
    print("=" * 60)

def create_ranking(results):
    """
    平均点によるランキングを作成・表示する
    
    Args:
        results (dict): 各学生の統計情報
    """
    if not results:
        return
    
    # 平均点でソート
    sorted_students = sorted(results.items(), key=lambda x: x[1]['平均点'], reverse=True)
    
    print("\n🏅 平均点ランキング")
    print("=" * 40)
    
    for rank, (student, stats) in enumerate(sorted_students, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"{rank:2d}"
        print(f"{medal} {student:<8} : {stats['平均点']:6.2f}点")
    
    print("=" * 40)

def main():
    """
    メイン処理
    """
    csv_file = "ダウンロード/課題2 (1).csv"
    
    print("📚 学生成績分析プログラム")
    print("=" * 60)
    
    # データを分析
    results = analyze_student_scores(csv_file)
    
    if results:
        # 結果を表示
        display_results(results)
        
        # ランキングを表示
        create_ranking(results)
        
        # 科目別分析も追加
        analyze_by_subject(csv_file)

def analyze_by_subject(csv_file):
    """
    科目別の分析を行う
    
    Args:
        csv_file (str): CSVファイルのパス
    """
    try:
        # CSVファイルを読み込む
        data = []
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    '名前': row['名前'],
                    '日付': row['日付'],
                    '科目': row['科目'],
                    'スコア': int(row['スコア'])
                })
        
        subjects = list(set(row['科目'] for row in data))
        
        print("\n📖 科目別分析")
        print("=" * 50)
        
        for subject in subjects:
            subject_scores = [row['スコア'] for row in data if row['科目'] == subject]
            
            print(f"\n【{subject}】")
            print(f"   平均点: {statistics.mean(subject_scores):6.2f}点")
            print(f"   最高点: {max(subject_scores):6d}点")
            print(f"   最低点: {min(subject_scores):6d}点")
            print(f"   受験者: {len(subject_scores):6d}人")
            
        print("=" * 50)
        
    except Exception as e:
        print(f"科目別分析でエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
