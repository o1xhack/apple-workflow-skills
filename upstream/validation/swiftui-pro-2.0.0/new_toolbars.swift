import SwiftUI
struct Sample: View { var body: some View {
 Text("A").toolbar {
  ToolbarItem(placement: .topBarPinnedTrailing) { Button("Save") {} }.contentMarginsRemoved().visibilityPriority(.high)
  ToolbarOverflowMenu { Button("Delete") {} }
 }.toolbarMinimizationBehavior(.onScrollDown, for: .navigationBar)
 .toolbarVisibility(.hidden, for: .statusBar)
} }
