import SwiftUI
struct Item: Identifiable { let id: Int }
extension ReorderDifference where CollectionID == ReorderableSingleCollectionIdentifier {
 func apply<Items>(to items: inout Items) where Items: RangeReplaceableCollection, Items.Element: Identifiable, Items.Element.ID == ItemID {
  let sourceIDs = Set(sources)
  var relocated: [Items.Element] = []
  items.removeAll { candidate in
   if sourceIDs.contains(candidate.id) { relocated.append(candidate); return true }
   return false
  }
  switch destination.position {
  case .before(let followingID):
   let insertionPoint = items.firstIndex { $0.id == followingID } ?? items.endIndex
   items.insert(contentsOf: relocated, at: insertionPoint)
  case .end: items.append(contentsOf: relocated)
  }
 }
}
struct Sample: View { @State private var items = [Item(id: 1), Item(id: 2)]
 var body: some View {
  ScrollView { LazyVStack {
   ForEach(items) { item in Text("\(item.id)").swipeActions { Button("Delete") {} } }.reorderable()
  }.reorderContainer(for: Item.self) { diff in diff.apply(to: &items) } }.swipeActionsContainer()
 }
}
